import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
import bisect

N,Q = map(int,input().split())
# STX = [list(map(int,input().split())) for _ in range (N)]
STX = []
vals = set()
for _ in range(N):
    s,t,x = map(int,input().split())
    STX.append((max(0,s-x), max(0,t-x), x))
    vals.add(max(0,s-x))
    vals.add(max(0,t-x))
D = [int(input()) for _ in range(Q)]
for d in D:
    vals.add(d)
vals = list(vals)
vals.sort()
L = len(vals)
mapping = [-1]*(L+1)
imos = [[] for _ in range(L+1)]
STX.sort(key=lambda x:x[2])
priority = 0 
for s,t,x in STX:
    s1 = bisect.bisect_left(vals, s)
    t1 = bisect.bisect_left(vals, t)
    imos[s1].append([1, priority, x])
    imos[t1].append([0, priority, x])
    priority += 1

import heapq
cur = -1
cur_priority = 10**9
que = [(cur_priority, cur)]
valid_priority = [True]*(N+1)
for i in range(L+1):
    for f,p,x in  imos[i]:
        if f:
            heapq.heappush(que, (p, x))
        else:
            valid_priority[p] = False
    
    while que[0][1]!=-1 and valid_priority[que[0][0]]==False:
        heapq.heappop(que)
    mapping[i] = que[0][1]

for d in D:
    d1 = bisect.bisect_left(vals, d)
    print(mapping[d1])

