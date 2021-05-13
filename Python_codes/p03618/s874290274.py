import sys
from collections import Counter


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    A = input()
    N = len(A)
    answer = N * (N - 1) // 2 + 1
    count = Counter(A)
    key = list(count.keys())
    for k in key:
        if count[k] > 1:
            answer -= count[k] * (count[k] - 1) // 2
    print(answer)


if __name__ == "__main__":
    main()
