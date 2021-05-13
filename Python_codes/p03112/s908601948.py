import sys
readline = sys.stdin.readline
from bisect import bisect_left
INF = 10 ** 11

def main():
    A, B, Q = map(int, readline().rstrip().split())
    S = [int(readline()) for _ in range(A)]
    T = [int(readline()) for _ in range(B)]

    for _ in range(Q):
        x = int(readline())
        s_right_idx = bisect_left(S, x)
        if s_right_idx == 0:
            s_right = S[s_right_idx]
            s_left = -INF
        elif s_right_idx == A:
            s_left = S[s_right_idx-1]
            s_right = INF
        else:
            s_left,  s_right = S[s_right_idx - 1], S[s_right_idx]
        
        t_right_idx = bisect_left(T, x)
        if t_right_idx == 0:
            t_right = T[t_right_idx]
            t_left = -INF
        elif t_right_idx == B:
            t_left = T[t_right_idx-1]
            t_right = INF
        else:
            t_left,  t_right = T[t_right_idx - 1], T[t_right_idx]

        s_left_d, s_right_d = x - s_left, s_right - x
        t_left_d, t_right_d = x - t_left, t_right - x

        res1 = max(s_right_d, t_right_d)
        res2 = max(s_left_d, t_left_d)
        res3 = min(s_right_d * 2 + t_left_d, t_right_d * 2 + s_left_d)
        res4 = min(s_right_d + t_left_d * 2, t_right_d + s_left_d * 2)
        res = min(res1, res2, res3, res4)
        print(res)


if __name__ == '__main__':
    main()