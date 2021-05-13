import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def enum_divisors(n):
    # 約数列挙

    divisors = []

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    return divisors


def main():
    n = int(readline())
    divs = enum_divisors(n)
    ans = 0

    for x in divs:
        m = n // x - 1
        if n - m * x < m:
            ans += m

    print(ans)


if __name__ == '__main__':
    main()
