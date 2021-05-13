MOD = 10 **9 + 7
INF = 10 ** 10
from heapq import heapify,heappop,heappush

def main():
    k,t = map(int,input().split())
    A = list(map(int,input().split()))
    if t == 1:
        print(k - 1)
        return
    A = [(-A[i],i) for i in range(t)]
    heapify(A)
    
    before = -1
    ans = 0
    for _ in range(k):
        p,i = heappop(A)
        if i != before:
            p += 1
            before = i
            heappush(A,(p,i))
        else:
            q,j = heappop(A)
            if q < 0:
                q += 1
                before = j
                heappush(A,(q,j))
                heappush(A,(p,i))
            else:
                p += 1
                ans += 1
                heappush(A,(p,i))
    print(ans)
if __name__ == '__main__':
    main()