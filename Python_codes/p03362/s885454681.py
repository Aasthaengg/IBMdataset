import math, sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import lru_cache
from heapq import heapify, heappop, heappush
from itertools import accumulate, combinations, permutations
input = sys.stdin.readline
mod = 10**9 + 7
ns = lambda: input().strip()
ni = lambda: int(input().strip())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

def main():
    n = ni()

    def primes(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if not is_prime[i]:
                continue
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
        return [i for i in range(n + 1) if is_prime[i]]

    p = primes(55555)
    ans = []
    i = 0

    for prime in p:
        if prime % 5 == 1:
            ans.append(prime)
            i += 1
        if i == n:
            break

    print(*ans)


if __name__ == '__main__':
    main()