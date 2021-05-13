import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def divisors(n):
    # 約数列挙

    divisors = []

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    return divisors


def main():
    from itertools import accumulate
    n, k = map(int, readline().split())
    a = list(map(int, readline().split()))
    s = sum(a)
    divs = divisors(s)
    divs.sort()

    ans = 1
    for div in divs:
        rem = [0] * n
        rem2 = [0] * n
        for i, x in enumerate(a):
            rem[i] = x % div
        rem.sort()
        for i in range(n):
            rem2[i] = div - rem[i]
        acc = list(accumulate(rem))
        acc2 = list(accumulate(rem2))
        for i in range(n):
            cnt = max(acc[i], acc2[-1] - acc2[i])
            if cnt <= k:
                ans = div
                break

    print(ans)


if __name__ == '__main__':
    main()
