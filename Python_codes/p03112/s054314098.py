from bisect import bisect_left
import sys
def main():
    input = sys.stdin.readline
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    INF = 10 ** 11
    S = [-INF] + S + [INF]
    T = [-INF] + T + [INF]
    for x in X:
        i = bisect_left(S, x)
        ls = x - S[i - 1]
        rs = S[i] - x
        j = bisect_left(T, x)
        lt = x - T[j - 1]
        rt = T[j] - x
        print(min(max(ls, lt), max(rs, rt), 2 * ls + rt, ls + 2 * rt, 2 * rs + lt, rs + 2 * lt))

if __name__ == '__main__':
    main()
