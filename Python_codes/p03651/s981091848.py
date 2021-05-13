from fractions import gcd
from functools import reduce

N, K = map(int, input().split())
A = list(map(int, input().split()))
A = set(A)

M = max(A)


def mgcd(x):
    return reduce(gcd, x)


if M < K:
    print("IMPOSSIBLE")
elif K in A:
    print("POSSIBLE")
else:
    G = mgcd(A)
    if K % G == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
