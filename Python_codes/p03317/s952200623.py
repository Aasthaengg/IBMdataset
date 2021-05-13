import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

least_g = (N-1) / (K-1)

if least_g.is_integer():
    print(int(least_g))
else:
    print(int(least_g)+1)
