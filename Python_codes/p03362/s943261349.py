import itertools
import math
import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


# MOD = 998244353


def get_primes(max=None, count=None):
    """
    素数列挙
    昇順にソートされています
    https://qiita.com/Ishotihadus/items/73e107271275611f05f2
    :param int max:
    :param int count:
    """
    assert max or count
    if count:
        raise NotImplementedError()
    if max <= 1:
        return []

    primes = [2]
    sieve = [False for _ in range(max + 1)]
    p = 3
    while p <= max:
        primes.append(p)
        sieve[p] = True
        if p <= math.sqrt(max):
            for i in range(p * (p | 1), max + 1, p * 2):
                sieve[i] = True
        while p <= max and sieve[p]:
            p += 2

    return primes


N = int(sys.stdin.buffer.readline())

is_prime = [False] * 55555 * 5
for p in get_primes(55555 * 5):
    is_prime[p] = True


def test(ans):
    for choices in itertools.combinations(ans, r=5):
        if is_prime[sum(choices)]:
            return False
    return True


# あーーー時間かかった
ans = []
for p in get_primes(55555):
    if p % 5 == 1:
        ans.append(p)

ans = ans[:N]
print(*ans)

# while True:
#     import random
#     ans = {2}
#     while len(ans) < 55:
#         ans.add(random.choice(primes))
#     print(ans)
#     if test(ans):
#         print(ans)
#         exit()
