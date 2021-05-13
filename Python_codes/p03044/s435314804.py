import sys
sys.setrecursionlimit(500*500)

graph = []
distance = []

def dfs(G, v, dist = 0):
    #print(v)
    distance[v-1] = dist

    for i in range(0,len(G[v-1]),2):
        #print(i, G[v-1][i])
        if distance[G[v-1][i]-1] != -1:
            continue
        dist += G[v-1][i+1]
        #print(1,1,dist)
        dfs(G, G[v-1][i], dist)
        dist -= G[v-1][i+1]

N = int(input())

for i in range(N):
    graph.append([])
    distance.append(-1)

for i in range(N-1):
    u, v, w = map(int, input().split())
    graph[u-1].append(v)
    graph[u-1].append(w)
    graph[v-1].append(u)
    graph[v-1].append(w)


#print(graph)
#print(distance)

dfs(graph, 1)

for i in range(N):
    if distance[i]%2 == 0:
        print(0)
    else:
        print(1)

#print(graph)
#print(distance)