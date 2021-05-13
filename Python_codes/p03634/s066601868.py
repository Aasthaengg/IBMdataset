import heapq
inf=float("inf")


def dijkstra(k):
    color=["white" for _ in range(n+1)]
    D=[inf for _ in range(n+1)]
    M=[[] for _ in range(n+1)]

    for a,b,c in ABC:
        M[a].append([c,b])
        M[b].append([c,a])

    D[k]=0
    color[k]="gray"
    queue=[[0,k]]
    heapq.heapify(queue)

    while len(queue)>0:
        u=heapq.heappop(queue)[1]
        color[u]="black"

        for i,j in M[u]:
            if color[j]!="black":
                if D[u]+i<D[j]:
                    D[j]=D[u]+i
                    color[j]="gray"
                    queue.append([D[j],j])

    return D


n=int(input())
ABC=[list(map(int,input().split())) for _ in range(n-1)]
q,k=map(int,input().split())
XY=[list(map(int,input().split())) for _ in range(q)]
D=dijkstra(k)

for x,y in XY:
    print(D[x]+D[y])