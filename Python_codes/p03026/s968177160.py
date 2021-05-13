import sys
sys.setrecursionlimit(10**8)
N = int(input())
AB = [tuple(map(int,input().split())) for i in range(N-1)]
C = list(map(int,input().split()))
C.sort()
es = [[] for i in range(N)]
for a,b in AB:
    a,b = a-1,b-1
    es[a].append(b)
    es[b].append(a)

score = 0
vscore = [-1]*N
vscore[0] = C.pop()

def dfs(v,p=-1):
    global score
    for to in es[v]:
        if to==p: continue
        vscore[to] = C.pop()
        score += min(vscore[v], vscore[to])
        dfs(to,v)
dfs(0)

print(score)
print(*vscore)