import sys
input = sys.stdin.readline

a, b, q = [int(x) for x in input().split()]
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
ans = []

import bisect
ans = []
for _ in range(q):
    x = int(input())
    idx_s = bisect.bisect_left(s, x)
    idx_t = bisect.bisect_right(t, x)
    s_ = []
    t_ = []
    if idx_s < a:
        s_.append(s[idx_s])
    if idx_t < b:
        t_.append(t[idx_t])
    if idx_s - 1 >= 0:
        s_.append(s[idx_s - 1])
    if idx_t - 1 >= 0:
        t_.append(t[idx_t - 1])
    res = float("inf")
    for i in s_:
        for j in t_:
            if (i >= x and j >= x) or (i <= x and j <= x):
                res = min(res, max(abs(i - x), abs(j - x)))
            else:
                res = min(res, abs(i - x) + abs(i - j), abs(j - x) + abs(i - j))
    ans.append(res)
for i in ans:
    print(i)

