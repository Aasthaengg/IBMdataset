N,M,P=map(int,input().split())
A=[0 for i in range(M)]
B=[0 for i in range(M)]
C=[0 for i in range(M)]
G=[dict() for i in range(N)]
H=[dict() for i in range(N)]
for i in range(M):
    A[i],B[i],C[i]=map(int,input().split())
    G[B[i]-1][A[i]-1]=C[i]
    H[A[i]-1][B[i]-1]=C[i]
reached1=[0 for i in range(N)]
q=[N-1]
while(len(q)>0):
    r=q.pop()
    reached1[r]=1
    for p in G[r]:
        if reached1[p]==0:
            q.append(p)
reached2=[0 for i in range(N)]
q=[0]
while(len(q)>0):
    r=q.pop()
    reached2[r]=1
    for p in H[r]:
        if reached2[p]==0:
            q.append(p)
reached=[reached1[i]*reached2[i] for i in range(N)]
vertex_list=[]
vertex_num=[-1 for i in range(N)]
tmp=1
for i in range(N):
    if reached[i]==1:
        vertex_list.append(i+1)
        vertex_num[i]=tmp
        tmp+=1
num_v=len(vertex_list)
edges=[]
for i in range(M):
    if reached[A[i]-1]==1 and reached[B[i]-1]==1:
        edges.append((vertex_num[A[i]-1],vertex_num[B[i]-1],P-C[i]))
inf=10**10
dist=[inf for i in range(num_v)]
dist[0]=0
#print(reached)
#print(edges)
#print(vertex_list)
#print(vertex_num)
#辺の緩和
for i in range(num_v):
    for edge in edges:
        if edge[0] != inf and dist[edge[1]-1] > dist[edge[0]-1] + edge[2]:
            dist[edge[1]-1] = dist[edge[0]-1] + edge[2]
            if i==num_v-1:
                print(-1)
                exit()
print(max(-dist[-1],0))
