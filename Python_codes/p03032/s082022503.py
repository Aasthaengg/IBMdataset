import heapq
from collections import deque
import copy

def main():
    n, k = map(int, input().split())
    v = deque([int(x) for x in input().split()])

    left_plus = 0
    left_minus_count = 0
    left_minus_list = []
    
    ans = 0
    sub = 0
    minus_list = []
    minus_count = 0
    heapq.heapify(minus_list)
    for i in range(n-1, max([-1, n-k-1]), -1):
        if v[i] >= 0:
            sub += v[i]
        else:
            heapq.heappush(minus_list, -v[i])
            minus_count += 1
        while n-i+minus_count > k and minus_list:
            sub -= heapq.heappop(minus_list)
            minus_count -= 1
        if n-i+minus_count > k:
            break
        if ans < sub:
            ans = sub
    
    for i in range(min([n, k])):
        if v[i] >= 0:
            left_plus += v[i]
        else:
            left_minus_list.append(-v[i])
            left_minus_count += 1
        
        sub = left_plus
        minus_count = left_minus_count
        minus_list = copy.deepcopy(left_minus_list)
        heapq.heapify(minus_list)
        while i+minus_count+1 > k and minus_list:
            minus_count -= 1
            sub -= heapq.heappop(minus_list)
        if i+minus_count+1 <= k and ans < sub:
            ans = sub
        sub = left_plus
        minus_count = left_minus_count
        minus_list = copy.deepcopy(left_minus_list)
        heapq.heapify(minus_list)
        for j in range(n-1, max([i, n-k+i+1]), -1):
            if v[j] >= 0:
                sub += v[j]
            else:
                minus_count += 1
                heapq.heappush(minus_list, -v[j])
            while minus_count+i+n-j+1 > k and minus_list:
                minus_count -= 1
                sub -= heapq.heappop(minus_list)
            
            if i+(n-j)+minus_count+1 > k:
                break
            if ans < sub:
                ans = sub
        
        
    print(ans)

if __name__ == "__main__":
    main()