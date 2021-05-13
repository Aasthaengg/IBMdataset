import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)
point = [0]*N
for _ in range(Q):
    p, x = map(int, input().split())
    point[p-1] += x
done = [-1]*N
def dfs(cur, fr, p):
    done[cur] = p
    for nex in G[cur]:
        if nex == fr: continue
        dfs(nex, cur, p+point[nex])
dfs(0, -1, point[0])
ans = []
for i in range(N):
    ans.append(done[i])
print(*ans)
