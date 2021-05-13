import math

N,D =[int(x) for x in input().split()]

X = []
Y = []

for i in range(N):
    x,y = [int(x) for x in input().split()]
    X.append(x)
    Y.append(y)

ans = 0

for i in range(N):
    r = math.sqrt(X[i] ** 2 + Y[i] ** 2)
    if r <= D:
        ans += 1

print(ans)