import sys

import numpy as np


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def make_prime(U):
    is_prime = np.zeros(U, np.bool)
    is_prime[2] = 1
    is_prime[3::2] = 1
    M = int(U ** 0.5) + 1
    for p in range(3, M, 2):
        if is_prime[p]:
            is_prime[p * p :: p + p] = 0
    return is_prime, is_prime.nonzero()[0]


def main():
    N = int(input())
    _, primes = make_prime(55556)

    r_5 = []
    for p in primes:
        if p % 5 == 1:
            r_5.append(p)
    # print(len(r_5))
    answer = r_5[:N]
    print(*answer)


if __name__ == "__main__":
    main()
