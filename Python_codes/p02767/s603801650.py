import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    X = list(map(int, readline().split()))
    ans = INF

    for i in range(1, 101):
        score = 0
        for x in X:
            score += (x - i) ** 2
        ans = min(ans, score)

    print(ans)


if __name__ == '__main__':
    main()
