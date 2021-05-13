N,Q = map(int,input().split())
STX = [tuple(map(int,input().split())) for i in range(N)]
D = [int(input()) for i in range(Q)]

starts = []
ends = []
for i,(s,t,x) in enumerate(STX):
    starts.append((s-x,i))
    ends.append((t-x,i))
starts.sort(key=lambda x:x[0], reverse=True)
ends.sort(key=lambda x:x[0], reverse=True)

import heapq
hq = []
heapq.heapify(hq)
delset = set()

ans = []
for d in D:
    while starts and starts[-1][0] <= d:
        _,i = starts.pop()
        x = STX[i][2]
        heapq.heappush(hq, x*N+i)
    while ends and ends[-1][0] <= d:
        _,i = ends.pop()
        delset.add(i)
    while hq:
        i = hq[0]%N
        if i in delset:
            heapq.heappop(hq)
        else:
            break
    if len(hq)==0:
        ans.append(-1)
    else:
        ans.append(hq[0]//N)

print(*ans, sep='\n')