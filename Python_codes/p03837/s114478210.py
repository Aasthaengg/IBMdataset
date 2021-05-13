import copy
n, m = map(int, input().split())
# 隣接行列
e = [[float('inf')]*n for i in range(n)]
for i in range(m):
    a, b,c = map(int, input().split())
    e[a-1][b-1]=c
    e[b-1][a-1]=c


ans=[[float('inf')]*n for i in range(n)]
d=copy.deepcopy(e)
# ワーシャルフロイド　全点最短経路、負の距離あっても可　o(n**3)
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j or k==i or k==j:
                    continue
                if d[i][j]==float('inf') and (d[i][k]==float('inf') or d[k][j]==float('inf')):
                    continue
                else:
                    if d[i][j] > d[i][k] + d[k][j]:
                        d[i][j]=d[i][k]+d[k][j]

warshall_floyd(d)
x=0
for i in range(n):
    for j in range(n):
        if e[i][j]!=float('inf'):
            if e[i][j]>d[i][j]:
                x+=1
print(x//2)