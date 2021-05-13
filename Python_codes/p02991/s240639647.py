import sys
input=sys.stdin.readline
import heapq

def dijkstra(graph,N,s):
    distance = {(i + 1, j): 1e7 for i in range(N) for j in range(3)}
    distance[s]=0
    q=[]
    heapq.heappush(q,(distance[s],s))
    while len(q)>0:
        cost,v=heapq.heappop(q)
        if cost>distance[v]:
            continue
        else:
            for w in graph[v]:
                if distance[w]>distance[v]+1:
                    distance[w]=distance[v]+1
                    heapq.heappush(q,(distance[w],w))
    return distance


if __name__ == '__main__':
    N,M=list(map(int,input().split()))
    E=[list(map(int,input().split())) for _ in range(M)]
    S,T=list(map(int,input().split()))
    graph={(i+1,j):[] for i in range(N) for j in range(3)}
    for e in E:
        graph[(e[0],0)].append((e[1],1))
        graph[(e[0],1)].append((e[1],2))
        graph[(e[0],2)].append((e[1],0))
    distance=dijkstra(graph,N,(S,0))
    d=distance[(T,0)]
    if d%3==0:
        print(d//3)
    else:
        print(-1)
