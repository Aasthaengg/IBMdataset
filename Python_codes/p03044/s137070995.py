import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

n = int(readline())
node = [[] for i in range(n)]

for i in range(n-1):
    u,v,w = map(int,readline().split())
    node[u-1].append((v-1,w))
    node[v-1].append((u-1,w))
ans = [-1]*n
ans[0] = 0
def dfs(fro, to, dis):
    ans[to] = dis%2
    for nxt, dist in node[to]:
        if nxt == fro:
            continue
        dfs(to, nxt, (dis+dist)%2)

for to,dis in node[0]:
    dfs(0,to,dis)

print("\n".join(map(str,ans)))

