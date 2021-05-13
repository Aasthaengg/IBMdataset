import sys
sys.setrecursionlimit(400000)
n,q=map(int,input().split())
ans=[0]*(n+1) #答え
score=[0]*(n+1) #xの総和
g=[[] for _ in range(n+1)] #グラフ
for i in range(n-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
for j in range(q):
    p,x=map(int,input().split())
    score[p]+=x

visited=[0]*(n+1)
def dfs(v):
    visited[v]+=1
    global ans
    ans[v]+=score[v]
    for i in range(len(g[v])):
        if visited[g[v][i]]==0:
            ans[g[v][i]]+=ans[v]
            dfs(g[v][i])
dfs(1)
print(" ".join(map(str, ans[1:])))
