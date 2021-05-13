import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    ans = INF

    for x in range(1, n):
        score = 0
        a = x
        b = n - a
        while a > 0:
            score += a % 10
            a //= 10
        while b > 0:
            score += b % 10
            b //= 10
        ans = min(ans, score)

    print(ans)


if __name__ == '__main__':
    main()
