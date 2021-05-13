import math

N, D = list(map(int, input().rstrip().split()))
r = 0
for i in range(N):
    X, Y = list(map(int, input().rstrip().split()))
    v = math.sqrt(X * X + Y * Y)
    if v <= D:
        r += 1

print(r)

