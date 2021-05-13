from bisect import bisect_left
import sys


sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]

    ans = []
    for _ in range(Q):
        x = int(input())

        i = bisect_left(S, x)
        if i == 0:
            s_left = None
        else:
            s_left = S[i - 1]
        if i < A:
            s_right = S[i]
        else:
            s_right = None

        j = bisect_left(T, x)
        if j == 0:
            t_left = None
        else:
            t_left = T[j - 1]

        if j < B:
            t_right = T[j]
        else:
            t_right = None

        # 左にいきっぱなし
        if s_left is not None and t_left is not None:
            ans1 = x - min(s_left, t_left)
        else:
            ans1 = INF

        # みぎにいきっぱなし
        if s_right is not None and t_right is not None:
            ans2 = max(s_right, t_right) - x
        else:
            ans2 = INF

        # 右神社 左寺
        if s_right is not None and t_left is not None:
            ans3 = min(s_right - x + s_right - t_left, x - t_left + s_right - t_left)
        else:
            ans3 = INF

        # 右寺，左神社
        if t_right is not None and s_left is not None:
            ans4 = min(t_right - x + t_right - s_left, x - s_left + t_right - s_left)
        else:
            ans4 = INF

        a = min(ans1, ans2, ans3, ans4)
        ans.append(a)

    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
