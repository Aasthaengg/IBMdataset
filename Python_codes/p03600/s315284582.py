n=int(input())
A=[]
for index in range(n):
    A.append(list(map(int,input().split())))

def warshall_floyd(G):
    h=len(G)

    res=0
    for x in range(h):
        for y in range(x+1,h):
            res+=G[x][y]

    check=[[0]*h for z in range(h)]
    for k in range(h):
        for i in range(h):
            for j in range(h):
                temp=G[i][k]+G[k][j]
                if temp==G[i][j]:
                   if i!=j and j!=k and k!=i:
                       check[i][j]=1
                elif temp<G[i][j]:
                    if i!=j and j!=k and k!=i:
                        check[i][j]=-1
    decrease=0             
    for p in range(h):
        for q in range(h):
            if check[p][q]==-1:
                return [False]
            elif check[p][q]==1:
                decrease+=G[p][q]
    else:
        return [True,res-decrease//2]


ans=warshall_floyd(A)
if not ans[0]:
    print(-1)
else:
    print(ans[1])

