MOD = 10**9+7
n, m = map(int, input().split())
X = list(map(int ,input().split()))
Y = list(map(int ,input().split()))
X.sort()
Y.sort()
mx, my = X[n-1], Y[m-1]
SX, SY = [0], [0]
for i in range(n):
    SX.append(mx-X[i])
for i in range(n):
    SX[i+1] += SX[i]
for i in range(m):
    SY.append(my-Y[i])
for i in range(m):
    SY[i+1] += SY[i]
xx = 0
for i in range(n):
    diff = mx-X[i]
    num = n-(i+1)
    tot = diff*num
    tot -= SX[n]-SX[i+1]
    xx += tot
yy = 0
for i in range(m):
    diff = my-Y[i]
    num = m-(i+1)
    tot = diff*num
    tot -= SY[m]-SY[i+1]
    yy += tot
print(xx*yy%MOD)
