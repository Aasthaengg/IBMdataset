import sys
from itertools import accumulate
def input(): return sys.stdin.readline().strip()


def get_sieve_of_eratosthenes(n):
    """
    エラトステネスの篩。√N以下の数に対して2から順にその数の倍数を消していく。
    計算量は「調和級数」になるのがミソ。具体的には
        N/2 + N/3 + N/5 + ... + N/(√N) = N * (1/2 + 1/3 + 1/5 + ... + 1/√N)
                                       = N * loglog(√N) (素数の逆数和の発散スピードがこれ)
                                       = N(loglogN - log2)
    """
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        return []
    prime = [1] * (n + 1)
    prime[0] = prime[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if not prime[i]: continue
        for j in range(i * 2, n + 1, i):
            prime[j] = 0
    return prime


def main():
    primes = get_sieve_of_eratosthenes(100000)
    like = [0] * 10**5
    for i in range(3, 10**5):
        if primes[i] and primes[(i + 1) // 2]:
            like[i] = 1
    like = list(accumulate(like))

    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        if l < 3: l = 3
        if r < 3:
            print(0)
            continue
        print(like[r] - like[l - 1])



if __name__ == "__main__":
    main()
