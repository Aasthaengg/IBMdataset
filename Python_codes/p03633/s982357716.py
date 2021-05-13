import math

N = int(input())
T = [int(input()) for _ in range(N)]

res = 1
for t in T:
    res = res * t // math.gcd(res, t)

print(res)
