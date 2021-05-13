import io
import os
from heapq import merge

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

MOD = 10 ** 9 + 7


def solve(N, K, A):
    assert 1 <= K <= len(A)
    A.sort()
    neg = [-x for x in A if x < 0][::-1]  # abs value only
    nonneg = [x for x in A if x >= 0]

    # Get product of the K smallest by absolute value
    # If there are no achievable nonneg products, then this will be the smallest negative product
    bestNeg = 1
    for i, x in enumerate(merge(neg, nonneg)):
        bestNeg *= x
        bestNeg %= MOD
        if i >= K - 1:
            break
    bestNeg = -bestNeg % MOD

    def getBestNonNeg(K):
        ans = 1
        if K % 2 == 1:
            # Num neg must be even, so we need an odd number of nonneg. Always take the highest nonneg
            if not nonneg:
                return None
            ans = nonneg.pop() % MOD
            K -= 1
        while K >= 2 and len(nonneg) >= 2 and len(neg) >= 2:
            if nonneg[-1] * nonneg[-2] < neg[-1] * neg[-2]:  # Take larger
                ans = (ans * neg.pop() * neg.pop()) % MOD
            else:
                ans = (ans * nonneg.pop() * nonneg.pop()) % MOD
            K -= 2
        while K >= 2 and len(neg) >= 2:
            ans = (ans * neg.pop() * neg.pop()) % MOD
            K -= 2
        while K >= 2 and len(nonneg) >= 2:
            ans = (ans * nonneg.pop() * nonneg.pop()) % MOD
            K -= 2
        if K == 0:
            return ans
        return None

    # Make largest nonnegative
    ans = getBestNonNeg(K)
    if ans is not None:
        return ans
    # Answer is negative
    return bestNeg


if False:
    from itertools import combinations
    import random

    random.seed(0)
    for t in range(10000000):
        N = random.randint(1, 10)
        A = [random.randint(-N, N) for i in range(N)]
        K = random.randint(1, N)
        ans = solve(N, K, A)
        expected = float("-inf")
        for combo in combinations(A, r=K):
            prod = 1
            for x in combo:
                prod *= x
            expected = max(expected, prod)
        print(N, K, A, ans, expected)
        assert ans == (expected % MOD)

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
print(solve(N, K, A))
