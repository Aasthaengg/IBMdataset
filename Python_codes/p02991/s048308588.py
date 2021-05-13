

import heapq as hq

def bfs(connections:list,s,t):
    inf = float('inf')
    costs =[[inf,inf,inf] for i in connections]
    visited = [[False,False,False] for i in connections]
    costs[s][0]=0
    q =[]
    hq.heappush(q,(0,0,s))

    while q:
        cost,step,node = hq.heappop(q)
        if visited[node][step]:
            continue
        visited[node][step] = True
        
        for target in connections[node]:
            if costs[target][(step+1)%3]>cost+1:
                costs[target][(step+1)%3]=cost+1
                hq.heappush(q,(cost+1,(step+1)%3,target)) 

    ans = costs[t][0]

    if ans == inf:
        print(-1)
    else:
        print(ans // 3)               


    



def resolve():
    N,M = map(int,input().split())

    connections = [[] for i in range(N)]
    for i in range(M):
        u,v = map(int,input().split())
        connections[u-1].append(v-1)

    S,T = map(int,input().split())

    bfs(connections,S-1,T-1)



if __name__ == "__main__":
    resolve()