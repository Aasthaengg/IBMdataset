import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    S = input()
    B = S.count("#")
    W = S.count(".")

    # 左からi文字目までの白の数
    n_white = []
    if S[0] == ".":
        n_white.append(1)
    else:
        n_white.append(0)
    for i in range(1, N):
        if S[i] == ".":
            n_white.append(n_white[-1] + 1)
        else:
            n_white.append(n_white[-1])

    # ....##### の並びにする.境目に関して全探索
    ans = min(B, W)
    for i in range(N):
        # 白に変える数
        cnt = i + 1 - n_white[i]

        # 黒に変える数
        cnt += n_white[-1] - n_white[i]

        if cnt < ans:
            ans = cnt

    print(ans)


if __name__ == "__main__":
    main()
