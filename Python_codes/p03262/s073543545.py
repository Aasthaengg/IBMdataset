N, X = map(int, input().split())
x = list(map(int, input().split()))

x.append(X)
from math import gcd
g = x[1] - x[0]
for i in range(N):
    g = gcd(g, (x[i+1] - x[i]))

print(abs(g))