from collections import deque
import sys
sys.setrecursionlimit(100000)

N=int(input())
AB=[list(map(int,input().split())) for _ in range(N-1)]
C=deque(sorted(map(int,input().split())))
edges=[[] for _ in range(N)]
for a,b in AB:
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

ps=[0]*N

def dfs(prev, curr):
    ps[curr]=C.pop()
    for dst in edges[curr]:
        if prev==dst:
            continue
        dfs(curr,dst)
dfs(-1,0)

ans=0
for a,b in AB:
    ans += min(ps[a-1],ps[b-1])

print(ans)
print(" ".join([str(p) for p in ps]))
