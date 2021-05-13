N,K=map(int,input().split())
if K>((N-1)*(N-2))//2:
    print(-1)
else:
    edge=[]
    for i in range(2,N+1):
        edge.append([1,i])
    addedge=((N-1)*(N-2))//2-K
    for i in range(2,N):
        for j in range(i+1,N+1):
            if addedge!=0:
                edge.append([i,j])
                addedge-=1
            else:
                break

    print(len(edge))
    for i in range(0,len(edge)):
        print(*edge[i])