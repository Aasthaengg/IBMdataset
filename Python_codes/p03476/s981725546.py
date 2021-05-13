import itertools


def get_sieve_of_eratosthenes(n):
    prime = [2]
    limit = int(n ** 0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


def main():
    Q = int(input())
    LR = [list(map(int, input().split())) for _ in range(Q)]
    N = 10 ** 5

    primes = set(get_sieve_of_eratosthenes(N))

    t = [0 for _ in range(N + 1)]
    for p in primes:
        a, b = divmod(p + 1, 2)
        if b == 0 and a in primes:
            t[p] += 1

    t = list(itertools.accumulate(t))

    for l, r in LR:
        print(t[r + 1] - t[l - 1])


main()

