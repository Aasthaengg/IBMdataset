#57 ABC137E
#ベルマンフォード

n,m,p=map(int,input().split())

abc=[list(map(int,input().split())) for _ in range(m)]
abc=[[a,b,p-c] for a,b,c in abc]
def BF(edges,num_v,source):
    #グラフの初期化
    inf=float("inf")
    dist=[inf for i in range(num_v)]
    dist[source-1]=0
  
    #辺の緩和
    neg=[False for _ in range(num_v)]
    for i in range(num_v-1):
        for edge in edges:
            if edge[0] != inf and dist[edge[1]-1] > dist[edge[0]-1] + edge[2]:
                dist[edge[1]-1] = dist[edge[0]-1] + edge[2]
    for i in range(num_v):
        for edge in edges:
            if edge[0] != inf and dist[edge[1]-1] > dist[edge[0]-1] + edge[2]:
                dist[edge[1]-1] = dist[edge[0]-1] + edge[2]
                neg[edge[1]-1]=True
            if neg[edge[0]-1]==True:
                neg[edge[1]-1]=True
    return dist,neg
dis,neg=BF(abc,n,1)
#print(dis,neg)
print(-1 if neg[-1] else max(0,-dis[-1]))