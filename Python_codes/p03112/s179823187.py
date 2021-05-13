import sys
from bisect import bisect_left

def solve():
    input = sys.stdin.readline
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    for _ in range(Q):
        x = int(input())
        si = bisect_left(S, x)
        ti = bisect_left(T, x)
        minLength = 10 **20
        both_left = 10 ** 20
        both_right = 10 ** 20
        s_t = 10 ** 20
        t_s = 10 ** 20
        if si > 0 and ti > 0: both_left = max(x - S[si-1], x - T[ti - 1])
        if si <= A - 1 and ti <= B - 1: both_right = max(S[si] - x, T[ti] - x)
        if si > 0 and ti <= B - 1: s_t = T[ti] - S[si-1] + min(x - S[si-1], T[ti] - x)
        if ti > 0 and si <= A - 1: t_s = S[si] - T[ti-1] + min(x - T[ti-1], S[si] - x)
        minLength = min([both_left, both_right, s_t, t_s])
        print(minLength)

    return 0

if __name__ == "__main__":
    solve()