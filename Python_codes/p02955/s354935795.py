from math import sqrt, floor
from itertools import accumulate

N, K = map(int, input().split())
A = list(map(int, input().split()))
assert N == len(A)

def divisors(n):
    ds = [d for d in range(1, floor(sqrt(n)) + 1) if n % d == 0]
    for d in ds:
        yield n // d
    if n == ds[-1] ** 2:
        ds.pop(-1)
    ds.reverse()
    for d in ds:
        yield d

S = sum(A)
for d in divisors(S):
    X = [a % d for a in A]
    X.sort()
    AC = accumulate(X)
    SB = accumulate(reversed([(d - x) % d for x in X]))
    SB = reversed(list(SB)[:-1])
    k = [a for a, s in zip(AC, SB) if a == s][0]
    if k <= K:
        print(d)
        break
