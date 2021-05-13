from heapq import heappop,heappush
from collections import defaultdict
N,Q = map(int,input().split())
event = []
for _ in range(N):
    s,t,x = map(int,input().split())
    event.append((s-x,1,x))
    event.append((t-x,2,x))

for i in range(Q):
    d = int(input())
    event.append((d,3,i))
event.sort()

memo = defaultdict(int)
nowStop = []
ans = [-1]*Q
for t,e,x in event:
    if e == 1:
        heappush(nowStop,x)
        memo[x] += 1
    if e == 2:
        memo[x] -= 1
    if e == 3:
        while nowStop:
            s = nowStop[0]
            if memo[s] == 0:
                heappop(nowStop)
            else:
                ans[x] = s
                break
for a in ans:
    print(a)