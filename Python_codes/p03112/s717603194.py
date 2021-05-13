import sys
from bisect import bisect_left

A, B, Q = map(int, sys.stdin.readline().split())
S = []
for _ in range(A):
    S.append(int(sys.stdin.readline()))
T = []
for _ in range(B):
    T.append(int(sys.stdin.readline()))

# S.sort()
# T.sort()
for _ in range(Q):
    x = int(sys.stdin.readline())

    #print("x", x)
    # 前後の神社、寺の距離を求める
    s_pos = bisect_left(S, x)
    if s_pos == 0:
        s_left = -float("inf")
    else:
        s_left = S[s_pos-1]
    if s_pos == A:
        s_right = float("inf")
    else:
        s_right = S[s_pos]
    #print("s", s_left, s_right)

    t_pos = bisect_left(T, x)
    if t_pos == 0:
        t_left = -float("inf")
    else:
        t_left = T[t_pos-1]
    if t_pos == B:
        t_right = float("inf")
    else:
        t_right = T[t_pos]
    #print("t", t_left, t_right)

    left_min = min(x - s_left, x - t_left)
    left_max = max(x - s_left, x - t_left)
    right_min = min(s_right - x, t_right - x)
    right_max = max(s_right - x, t_right - x)
    print(min(left_max, right_max,
                2 * (x - s_left) + (t_right - x), 2 * (x - t_left) + (s_right - x),
                2 * (t_right - x) + (x - s_left), 2 * (s_right - x) + (x - t_left)))