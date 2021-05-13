import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from math import gcd
from functools import reduce
def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    M = max(A)

    if reduce(gcd, A) != 1:
        print("not coprime")
        return

    # linear sieve
    sieve = list(range(M + 1))
    primes = []
    for i in range(2, M + 1):
        if sieve[i] == i:
            primes.append(i)
        for p in primes:
            if sieve[i] < p or i * p > M:
                break
            sieve[i * p] = p

    # remove prime duplicates
    f = list(range(M + 1))
    g = [1] * (M + 1)
    for i in range(2, M + 1):
        j = 0
        for j in range(i * i, M + 1, i * i):
            g[j] = i
        f[i] = f[i // g[i]]

    # prime factorization
    used = [False] * (M + 1)
    for a in map(lambda a : f[a], A):
        while a != 1:
            p = sieve[a]
            if used[p]:
                print("setwise coprime")
                return
            used[p] = True
            a //= p
    print("pairwise coprime")
resolve()