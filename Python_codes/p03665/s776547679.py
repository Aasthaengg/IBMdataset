import sys
import math

N, P = map(int, sys.stdin.readline().strip().split())
A = map(int, sys.stdin.readline().strip().split())


def nCr(n, r):
    return math.factorial(n) // math.factorial(n - r) // math.factorial(r)

evens = 0
odds = 0
for a_i in A:
    if a_i % 2 == 0:
        evens += 1
    else:
        odds += 1

# 偶数の服からa個、奇数の袋から2b個取れば良い
if P == 0:
    ans = 2**(evens)
    tmp = 0
    for i in range(0, odds+1, 2):
        tmp += nCr(odds, i)
    ans *= tmp
# 偶数の服からa個、奇数の袋から2b+1個取れば良い
else:
    ans = 2**(evens)
    tmp = 0
    for i in range(1, odds+1, 2):
        tmp += nCr(odds, i)
    ans *= tmp

print(ans)