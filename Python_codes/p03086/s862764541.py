import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()
    N = len(S)

    ans = 0

    for i in range(N):
        for j in range(i, N):
            for k in range(i, j + 1):
                if S[k] not in ("A", "C", "G", "T"):
                    break
            else:
                ans = max(ans, j - i + 1)

    print(ans)


if __name__ == '__main__':
    main()
