import sys
from collections import Counter

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    S = list(input())
    N = len(S)
    ans = N * (N - 1) // 2 + 1
    c = Counter(S)
    for k, v in c.items():
        if v > 1:
            ans -= v * (v - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
