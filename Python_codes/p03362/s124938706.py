import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def prime_numbers(n):
    if n < 2:
        return []

    m = (n + 1) // 2
    p = [1] * m
    for i in range(1, int((n ** 0.5 - 1) / 2) + 1):
        if p[i]:
            p[2 * i * (i + 1) :: 2 * i + 1] = [0] * (((m - 1) - 2 * i * (i + 1)) // (2 * i + 1) + 1)

    a = [2 * i + 1 for i in range(m) if p[i]]
    a[0] = 2
    return a


def main():
    N = int(readline())

    primes = prime_numbers(55555)
    ans = []
    for p in primes:
        if p % 5 == 1:
            ans.append(p)
        if len(ans) == N:
            break

    print(*ans)
    return


if __name__ == '__main__':
    main()
