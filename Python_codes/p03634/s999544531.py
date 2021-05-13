import sys
sys.setrecursionlimit(10**9)

N = int(input())
tree = [[] for _ in range(N)]
for i in range(N-1):
    a,b,c = map(int,input().split())
    tree[a-1].append((b-1,c))
    tree[b-1].append((a-1,c))

Q,K = map(int,(input().split()))

dis = [-1]*N
dis[K-1] = 0
def dfs(v,d):
    for i in tree[v]:
        d = dis[v]
        next,c = i
        if dis[next] == -1:
            d += c
            dis[next] = d
            dfs(next,d)
dfs(K-1,0)

for i in range(Q):
    x,y = map(int,(input().split()))
    print(dis[x-1]+dis[y-1])