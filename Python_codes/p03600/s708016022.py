#D問題
import copy

N = int(input())
A = [list(map(int,input().split())) for i in range(N)]
G = copy.deepcopy(A)
whole = 0
for i in range(N):
    for j in range(N):
        whole+=A[i][j]


#print(A,G)
#warshall_floyd法
def warshall_floyd(dist):
    global N
    #dist[i][j]: iからjへの最短距離
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])

warshall_floyd(G)
#print(A,G)

flag = 0
ans = 0
for i in range(N):
    for j in range(N):
        if A[i][j] != G[i][j]:
            flag = 1
        else:
            for k in range(N):
                if k != i and k != j:
                    #print(G[i][j],G[i][k]+G[k][j])
                    if G[i][j] == G[i][k] + G[k][j]:
                        ans+=A[i][j]
                        #print(A[i][j])
                        break
                
            
if flag == 1:
    print(-1)
else:
    print((whole-ans)//2)