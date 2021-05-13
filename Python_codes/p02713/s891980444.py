# aaa
from math import gcd
# gcd: to get 最大公約数

k = int(input())
gg = [0] * k
ans = 0
for i in range(1, k + 1):
    for j in range(1, k + 1):
        temp = gcd(i, j)
        for l in range(1, k + 1):
            ans += gcd(temp, l)

print(ans)
