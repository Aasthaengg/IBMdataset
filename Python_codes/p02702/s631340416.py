# https://atcoder.jp/contests/abc164/tasks/abc164_d

from operator import mul
from functools import reduce
from collections import defaultdict

def combination(n, r):
    if not 0 <= r <= n: return 0
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

S = input()

res = 0

T = [0]
x = 0
L = len(S)
for i, s in zip(range(L),reversed(S)):
    """ 累積和 """
    x = (int(s)*pow(10,i,2019) + x)%2019
    T.append(x)

reminder = [0]*2019
for i in range(L+1):
    reminder[T[i]%2019] += 1

for c in reminder:
    res += combination(c,2)

print(res)