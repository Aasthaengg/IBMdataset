import sys
import bisect
N, K = map(int, sys.stdin.readline().split())
V = list(map(int, sys.stdin.readline().split()))

ans = 0

max_take = min(N, K)

for A in range(max_take + 1):
    for B in range(max_take - A + 1):
        #if A > 0 and B > 0:
        list = V[:A] + V[N - B:]
        total_sum = sum(list) 
        list.sort()
        n = bisect.bisect_left(list, 0)
        if n <= K - (A + B):
            total_sum -= sum(list[:n])
        else:
            total_sum -= sum(list[:K - (A + B)])
        '''
        elif A == 0 and B > 0:
            list = V[N - B:]
            total_sum = sum(list)
            list.sort()
            n = bisect.bisect_left(list, 0)
            if n <= K - (A + B):
                total_sum -= sum(list[:n])
            else:
                total_sum -= sum(list[:K - (A + B)])
        elif A > 0 and B == 0:
            list = V[:A]
            total_sum = sum(list)
            list.sort()
            n = bisect.bisect_left(list, 0)
            if n <= K - (A + B):
                total_sum -= sum(list[:n])
            else:
                total_sum -= sum(list[:K - (A + B)])
        else:
            continue'''
        
        if total_sum > ans:
            ans = total_sum
            
print(ans)