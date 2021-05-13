import sys

input = sys.stdin.readline


def get_primes(n):
    sieve = [1] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i:: 2 * i] = [0] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def main():
    N = int(input())
    primes = get_primes(55555)
    ans = []
    for p in primes:
        if len(ans) == N:
            break

        if p % 5 == 1:
            ans.append(p)

    print(*ans)


if __name__ == '__main__':
    main()
