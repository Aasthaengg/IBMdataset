import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    S = input()
    N = len(S)
    w = int(input())
    ans = []
    for i in range(0, N, w):
        ans.append(S[i])

    print(*ans, sep="")


if __name__ == "__main__":
    main()
