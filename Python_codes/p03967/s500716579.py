import sys
from collections import Counter

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    S = list(input())
    c = Counter(S)
    ans = (c["g"] - c["p"]) // 2
    print(ans)


if __name__ == "__main__":
    main()
