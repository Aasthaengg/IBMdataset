# cook your dish here
def dijkstra_back(s,t,n,w,cost):
    #sからtへの最短経路の経路復元
    prev = [s] * n #最短経路の直前の頂点
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0
    
    while True:
        v = -1
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
               break
        used[v] = True
        
        for i in range(n):
            if d[i] > d[v] + cost[v][i]: 
                d[i] = d[v] + cost[v][i]
                prev[i] = v
        
    path = [t]
    while prev[t] != s:
        path.append(prev[t])
        prev[t] = prev[prev[t]]
    path.append(s)
    path = path[::-1]
    return path

################################
n,w = map(int,input().split()) #n:頂点数　w:辺の数

cost = [[float("inf") for i in range(n)] for i in range(n)] 
#cost[u][v] : 辺uvのコスト(存在しないときはinf この場合は10**10)
for i in range(w):
    x,y,z = map(int,input().split())
    cost[x-1][y-1] = z
    cost[y-1][x-1] = z

check = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(i+1,n):
        tmp = dijkstra_back(i,j,n,w,cost)
        #print(tmp)
        for k in range(len(tmp)-1):
            #print(tmp[k],tmp[k+1])
            check[min(tmp[k],tmp[k+1])][max(tmp[k],tmp[k+1])] = 1

#print(check)

#exit()

print(w - sum(map(sum, check)))

#print(dijkstra_back(0,1,n,w,cost))