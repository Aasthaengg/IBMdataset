import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    if N == 1:
        print(1)
        return

    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    cnt = defaultdict(int)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            dx = X[j] - X[i]
            dy = Y[j] - Y[i]
            cnt[(dx, dy)] += 1

    cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    ans = N - cnt[0][1]
    print(ans)


if __name__ == "__main__":
    main()
