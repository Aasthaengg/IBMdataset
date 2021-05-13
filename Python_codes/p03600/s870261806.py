# ワーシャルフロイド　全点最短経路、負の距離あっても可　o(n**3)
def warshall_floyd(d,ans):
    #d[i][j]: iからjへの最短距離
    flag=True
    for i in range(n):
        for j in range(n):
            x=d[i][j]
            y=float('inf')
            for k in range(n):
                if k!=i and k!=j:
                    y = min(d[i][k] + d[k][j],y)
            if x==y:
                ans-=y
            elif x<y:
                continue
            else:
                flag=False
                break

    return flag,ans

##############################
n=int(input())

d = [list(map(int, input().split())) for i in range(n)]
ans=0
for i in range(n):
    ans+=sum(d[i])


a1,a2=warshall_floyd(d,ans)

if a1:
    print(a2//2)
else:
    print(-1)