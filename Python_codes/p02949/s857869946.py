def BellmanFord(edges,num_v,source):
    #グラフの初期化
    inf=float("inf")
    dist=[inf for i in range(num_v)]
    dist[source-1]=0
    flag = False

    #辺の緩和
    for i in range(num_v):
        for edge in edges:
          if edge[0] != inf and dist[edge[1]-1] > dist[edge[0]-1] + edge[2]:
            dist[edge[1]-1] = dist[edge[0]-1] + edge[2]
            if i==num_v-1:
                if edge[1] == num_v:
                    return -1
                else:
                    dist[edge[1]-1] = -inf
                    flag = True
    if flag:
        for i in range(num_v):
            for edge in edges:
                if dist[edge[1]-1]>dist[edge[0]-1] + edge[2]:
                    dist[edge[1]-1] = dist[edge[0]-1] + edge[2]
                    if edge[1] == num_v :
                        return -1

    return dist

N,M,P = [int(x) for x in input().split()]
gp = []
for _ in range(M):
    A,B,C = [int(x) for x in input().split()]
    gp.append([A,B,P-C])

li = BellmanFord(gp,N,1)
if(li==-1):
    print(-1)
else:
    print(max(0,-li[N-1]))
