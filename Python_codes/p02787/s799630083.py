import sys
from fractions import Fraction
input = sys.stdin.readline

h, n = list(map(int, input().split()))

mp = 0

a = []
b = []

for i in range(n):
    ai, bi = list(map(int, input().split()))
    a.append(ai)
    b.append(bi)

dp = [0] * (h+1)

dp[0] = 0

for i in range(1, h+1):
    m = 1000000000
    for j in range(n):
        l = 0
        if i - a[j] < 0:
            l = b[j]
        else:
            l = b[j] + dp[i - a[j]]
        m = min(l, m)
    dp[i] = m

print(dp[h])

