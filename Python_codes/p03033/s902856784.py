from heapq import heappop,heappush
from collections import defaultdict

N,Q = map(int,input().split())
events = []
for _ in range(N):
    s,t,x = map(int,input().split())
    events.append((s-x,1,x))
    events.append((t-x,2,x))

for _ in range(Q):
    d = int(input())
    events.append((d,3,0))

events.sort()

minimumStop = [float("INF")]
stopCount = {float("INF"):1}

for sec,e,x in events:
    if e == 1:
        heappush(minimumStop,x)
        if x not in stopCount:
            stopCount[x] = 0
        stopCount[x] += 1
    if e == 3:
        while stopCount[minimumStop[0]] == 0:
            heappop(minimumStop)
        if minimumStop[0] == float("INF"):
            print(-1)
        else:
            print(minimumStop[0])
    if e == 2:
        stopCount[x] -= 1
