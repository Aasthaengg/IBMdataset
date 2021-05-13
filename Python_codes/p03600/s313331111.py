import copy


def warshalFloyd(n):
    G=[list(map(int,input().split())) for _ in range(n)]
    D=copy.deepcopy(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j]=min(G[i][j],G[i][k]+G[k][j])

    return G if G==D else -1


n=int(input())
Graph=warshalFloyd(n)
if Graph==-1:print(-1);exit()

for k in range(n):
    for i in range(n):
        for j in range(n):
            if Graph[i][j]!=0 and Graph[i][k]!=0 and Graph[k][j]!=0:
                if Graph[i][j]==Graph[i][k]+Graph[k][j]:
                    Graph[i][j]=0

ans=0
for i in range(n):
    ans +=sum(Graph[i])
print(ans//2)