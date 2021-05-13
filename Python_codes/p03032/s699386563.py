# D - equeue

import heapq

n, k = map(int, input().split())
v = list(int(x) for x in input().split())

ans = 0
for l in range(k+1):
    for r in range(k+1-l):
        if l+r>n:
            continue
        tmp = 0
        s = []
        for i in range(l):
            tmp += v[i]
            heapq.heappush(s, v[i])

        for i in range(n-r, n):
            tmp += v[i]
            heapq.heappush(s, v[i])
            
        for i in range(k-l-r):
            if len(s)==0:
                break
            if s[0]>0:
                break
            tmp -= heapq.heappop(s)
        
        ans = max(ans, tmp)

print(ans)