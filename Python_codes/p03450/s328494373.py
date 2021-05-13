N,M = map(int, input().split())
L = [0]*M
R = [0]*M
D = [0]*M
for i in range(M):
    L[i], R[i], D[i] = map(int, input().split())
    
G = [[] for _ in range(N)]
for i in range(M):
    G[L[i]-1].append([R[i]-1, D[i]])
    G[R[i]-1].append([L[i]-1, -D[i]])
    
ans = "Yes"
visited = ["?"]*N
for i in range(N):
    if visited[i] == "?":
        q = [[i, 0]]
        visited[i] = 0
        while len(q) > 0:
            temp = q.pop(-1)
            pos = temp[0]
            d = temp[1]
            for j in range(len(G[pos])):
                if visited[G[pos][j][0]] == "?":
                    q.append([G[pos][j][0], d+G[pos][j][1]])
                    visited[G[pos][j][0]] = d+G[pos][j][1]
                elif visited[G[pos][j][0]] != d+G[pos][j][1]:
                    ans = "No"
                    break

print(ans)