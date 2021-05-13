MOD = 10 ** 9 + 7


def solve(N, K):
    ans = 0
    numExact = [0] * (K + 1)
    for g in reversed(range(1, K + 1)):
        # Count number of sequences where every element is a multiple of g
        # The gcd of such sequence is at least g
        numGreaterEq = pow(K // g, N, MOD)
        # But we want exact, so subtract the sequences where the gcd is a multiple of g
        numGreater = 0
        for multipleG in range(2 * g, K + 1, g):
            numGreater += numExact[multipleG]
        numExact[g] = numGreaterEq - numGreater
        ans += g * numExact[g]
        ans %= MOD

    return ans


if False:
    import random
    from itertools import product
    from math import gcd

    random.seed(0)
    for _ in range(10000):
        N = random.randint(1, 1)
        K = random.randint(1, 10)

        brute = 0
        for arr in product(range(1, K + 1), repeat=N):
            g = 0
            for x in arr:
                g = gcd(g, x)
            brute += g
        brute = brute % MOD

        ans = solve(N, K)
        # print(N, K, ans, brute)
        assert ans == brute


N, K = [int(x) for x in input().split()]

print(solve(N, K))
