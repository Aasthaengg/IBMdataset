import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    S = input()
    N = len(S)

    # n文字まで見て最後が1文字か2文字か
    dp_1 = [0] * N
    dp_2 = [0] * N
    dp_1[0] = 1
    dp_2[1] = 1
    if S[0] != S[1]:
        dp_1[1] = 2

    for i in range(2, N):
        # 2 -> 1
        dp_1[i] = max(dp_2[i - 1] + 1, dp_1[i])

        # 2 -> 2
        if S[i - 2 : i] != S[i : i + 2]:
            dp_2[i] = max(dp_2[i - 2] + 1, dp_2[i])

        # 1 -> 2
        dp_2[i] = max(dp_1[i - 2] + 1, dp_2[i])

        # 1 -> 1
        if S[i - 1] != S[i]:
            dp_1[i] = max(dp_1[i - 1] + 1, dp_1[i])

    ans = max(dp_1[-1], dp_2[-1])
    print(ans)


if __name__ == "__main__":
    main()
