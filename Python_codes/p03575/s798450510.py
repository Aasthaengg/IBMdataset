from collections import deque
n,m = map(int,input().split())
L =[list(map(int, input().split())) for _ in range(m)]
#print(L)
cnt = 0
for i in range(m):
    G = [[] for _ in range(n)]
    
    for j in range(m):
        if i == j:
            continue
        a,b = L[j][0],L[j][1]
        #print(a-1,b-1)
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    #print(G)
    Q = deque()
    Q.append(0)
    visited = [0]*n
    visited[0] = 1
    while Q:
        q = Q.pop()
        for g in G[q]:
            if visited[g] == 0:
                visited[g] = 1
                #print(visited)
                Q.append(g)

    if 0 in visited:
        cnt +=1
print(cnt)