n,m,p=map(int,input().split())
A=[]
for i in range(m):
    a,b,c=map(int,input().split())
    A.append((a,b,c-p))

def BellmanFord(edges,num_v,source):
    #グラフの初期化
    inf=float("inf")
    dist=[-inf for i in range(num_v)]
    dist[source-1]=0
  
    #辺の緩和
    buf=0
    for i in range(num_v*2):
        for edge in edges:
            if dist[edge[1]-1] < dist[edge[0]-1] + edge[2]:
                dist[edge[1]-1] = dist[edge[0]-1] + edge[2]
                if i>=num_v:
                    dist[edge[1]-1] =inf
        if i==num_v-1:
            buf=dist[-1]
    if dist[-1]!=buf or dist[-1]==-inf:
        return -1
    return max(dist[-1],0)

x=BellmanFord(A,n,1)
print(x)