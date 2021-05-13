from math import exp
from math import log

n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
Z = [abs(X[i] - Y[i]) for i in range(n)]
D1 = sum(Z)
try:
    D2 = exp((1 / 2) * log(sum((Z[i] ** 2) for i in range(n))))
    D3 = exp((1 / 3) * log(sum((Z[i] ** 3) for i in range(n))))
except ValueError:
    D2 = 0
    D3 = 0
Di = max(Z)
print("{:.5f}".format(D1))
print("{:.5f}".format(D2))
print("{:.5f}".format(D3))
print("{:.5f}".format(Di))