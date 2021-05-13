import sys
input = sys.stdin.readline
from math import gcd

n, res = int(input()), 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            res += gcd(i, gcd(j, k))
print(res)