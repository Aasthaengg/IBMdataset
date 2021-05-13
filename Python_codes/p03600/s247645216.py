import copy
N=int(input())



def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d


G=[]
for i in range(N):
    A=list(map(int, input().split()))
    G.append(A)

H=copy.deepcopy(G)

#print(H, G)
H=warshall_floyd(H)



for i in range(N):
    for j in range(N):
        if G[i][j]!=H[i][j]:
            print(-1)
            exit()
T=copy.deepcopy(H)
for k in range(N):
    for i in range(N):
        for j in range(N):
            if H[i][j]==H[i][k] + H[k][j] and i!=k and j!=k:
                T[i][j]=0
ans=0
for i in range(N):
    ans+=sum(T[i])
print(ans//2)



