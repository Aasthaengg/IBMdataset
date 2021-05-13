n,m = map(int,input().split())
INF = 10**9+7

def F(j,i):
    return (i*(j-i))%INF
dx = []
px = 0
sx = 0
for x in map(int,input().split()):
    dx.append(x-px)
    px = x
dy = []
py = 0
sy = 0
for y in map(int,input().split()):
    dy.append(y-py)
    py = y

for i in range(1,n):
    sx = (sx+(dx[i]*F(n,i))%INF)%INF 
for i in range(1,m):
    sy = (sy+(dy[i]*F(m,i))%INF)%INF
print((sx*sy)%INF)
