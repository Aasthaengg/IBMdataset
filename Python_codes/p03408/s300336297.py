import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter
    N = int(readline())
    blue = Counter()
    red = Counter()

    for _ in range(N):
        s = input()
        blue[s] += 1

    M = int(readline())

    for _ in range(M):
        s = input()
        red[s] += 1

    ans = 0

    for key in blue.keys():
        score = blue[key] - red[key]
        ans = max(ans, score)

    print(ans)


if __name__ == '__main__':
    main()
