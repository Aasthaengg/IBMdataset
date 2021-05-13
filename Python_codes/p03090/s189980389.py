import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())

    ans = []
    S = sum(range(1, N + 1))
    if N % 2 == 0:
        S -= N + 1
        for i in range(1, N + 1):
            for j in range(i + 1, N + 1):
                if i + j == N + 1:
                    continue
                else:
                    ans.append((i, j))
    else:
        S -= N
        for i in range(1, N + 1):
            for j in range(i + 1, N + 1):
                if i + j == N:
                    continue
                else:
                    ans.append((i, j))

    M = len(ans)
    print(M)
    for i, j in ans:
        print(i, j)


if __name__ == "__main__":
    main()
