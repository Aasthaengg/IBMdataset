from math import gcd
N = int(input())

res = 1
for _ in range(N):
    T = int(input())
    res = res*T//gcd(res, T)

print(res)