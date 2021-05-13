import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a = [int(input()) for _ in range(5)]
    b = [(x + 9) // 10 * 10 for x in a]

    ans = INF
    for i in range(5):
        ans = min(ans,sum(b) - b[i] + a[i])

    print(ans)


if __name__ == '__main__':
    main()
