# https://atcoder.jp/contests/abc142/tasks/abc142_d
# 公約数とは、最大公約数の約数

import sys
import math
from functools import reduce

input = sys.stdin.readline

A, B = [int(x) for x in input().split()]


def gcd(*numbers):
    return reduce(math.gcd, numbers)

# 素因数分解
# 考え方：1~√nまで実際に割れるか試せば良いが、割れた場合は割れる限りその数で割り続ける
# 計算量：O(√n)
def prime_factorize(n):
    i = 2
    primes = []
    while i * i <= n:
        if n % i != 0:
            i += 1
            continue
        exp = 0
        while n % i == 0:
            exp += 1
            n = n // i
        primes.append([i, exp])
        i += 1
    # 最後に残った数は1か素数にしかならない
    if n != 1:
        primes.append([n, 1])
    return primes

g = gcd(A, B)
divisors = prime_factorize(g)
print(len(divisors)+1)

