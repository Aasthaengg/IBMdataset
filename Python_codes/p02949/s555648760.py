#入力
n,m,r=map(int,input().split())
abc=[list(map(int,input().split())) for _ in [0]*m]
#グラフ
g=[[] for _ in [0]*n]
[g[a-1].append([b-1,c]) for a,b,c in abc]

#逆辺
g2=[[] for _ in [0]*n]
[g2[b-1].append([a-1,c]) for a,b,c in abc]

#前処理用のDFS
def remove_edge(graph,start):
    q=[start]
    memo=[True for _ in range(n)]
    memo[start]=False
    while q:
        qq=q.pop()
        for i,j in graph[qq]:
            if memo[i]:
                q.append(i)
                memo[i]=False
    return {i for i,j in enumerate(memo) if j==True}

#前処理
rmv=remove_edge(g,0)|remove_edge(g2,n-1)
for i in rmv:
    g[i]=[]
for i in range(n):
    for j in g[i]:
        if j[0] in rmv:
            g[i].remove(j)

#ベルマンフォード
dist=[-10**15 for _ in [0]*n]
dist[0]=0

for k in range(n):
    for p in range(n):
        for i,j in g[p]:
            dist[i]=max(dist[i],dist[p]+j-r)
    if k==n-2:
        d1=[t for t in dist]
    if k==n-1:
        d2=[t for t in dist]
        
#1からでもnの間に負の閉路があるときは-1
if d1==d2:
    print(max(d1[-1],0))
else:
    print(-1)