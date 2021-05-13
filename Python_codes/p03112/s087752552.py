import sys
import bisect

input = sys.stdin.readline


def main():
    A, B, Q = [int(x) for x in input().split()]
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    for _ in range(Q):
        x = int(input())
        si = bisect.bisect_left(S, x)
        ti = bisect.bisect_left(T, x)
        sl = -float("inf")
        if si != 0:
            sl = S[si - 1]
        sr = float("inf")
        if si != A:
            sr = S[si]
        tl = -float("inf")
        if ti != 0:
            tl = T[ti - 1]
        tr = float("inf")
        if ti != B:
            tr = T[ti]

        tmp1 = max(x - sl, x - tl)
        tmp2 = max(sr, tr) - x
        tmp3 = 2 * (x - sl) + tr - x
        tmp4 = 2 * (x - tl) + sr - x
        tmp5 = x - sl + 2 * (tr - x)
        tmp6 = x - tl + 2 * (sr - x)

        print(min(tmp1, tmp2, tmp3, tmp4, tmp5, tmp6))


if __name__ == '__main__':
    main()
