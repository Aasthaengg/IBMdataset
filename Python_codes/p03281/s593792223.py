import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())

    def enum_divisors(n):
        # 約数列挙

        divisors = []

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)

        return divisors

    ans = 0
    for i in range(1, N + 1, 2):
        divs = enum_divisors(i)
        if len(divs) == 8:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
