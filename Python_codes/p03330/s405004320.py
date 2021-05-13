N,C=map(int,input().split())
D=[list(map(int,input().split())) for i in range(C)]
c=[list(map(int,input().split())) for i in range(N)]

res=[[] for i in range(3)]
for mod in range(3):
    for color in range(C):
        dif=0
        for i in range(N):
            for j in range(N):
                if (i+j+2)%3==mod:
                    dif+=D[c[i][j]-1][color]
        res[mod].append([dif,color])
for i in range(3):
    res[i].sort()
ans=10**10
for i in range(3):
    for j in range(3):
        for k in range(3):
            if((res[0][i][1]!=res[1][j][1])and(res[1][j][1]!=res[2][k][1])and(res[2][k][1]!=res[0][i][1])):
                ans=min(ans,res[0][i][0]+res[1][j][0]+res[2][k][0])
print(ans)