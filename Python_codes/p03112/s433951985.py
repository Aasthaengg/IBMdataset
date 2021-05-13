import sys
input = sys.stdin.readline

a, b, q = [int(x) for x in input().split()]
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
x = [int(input()) for _ in range(q)]
s.sort()
t.sort()

import bisect

for i in x:
    s_idx = bisect.bisect_right(s, i)
    ans = 10 ** 18
    if s_idx == 0:
        s_ = [s[0]]
    elif s_idx >= a:
        s_ = [s[-1]]
    else:
        s_ = [s[s_idx], s[s_idx - 1]]
    for j in s_:
        tmp = abs(i - j)
        t_idx = bisect.bisect_right(t, j)
        if t_idx == 0:
            tmp += abs(j - t[0])
        elif t_idx >= b:
            tmp += abs(j - t[-1])
        else:
            tmp += min(abs(j - t[t_idx]), abs(j - t[t_idx - 1]))
        ans = min(tmp, ans)
    
    t_idx = bisect.bisect_right(t, i)
    if t_idx == 0:
        t_ = [t[0]]
    elif t_idx >= b:
        t_ = [t[-1]]
    else:
        t_ = [t[t_idx], t[t_idx - 1]]
    for j in t_:
        tmp = abs(i - j)
        s_idx = bisect.bisect_right(s, j)
        if s_idx == 0:
            tmp += abs(j - s[0])
        elif s_idx >= a:
            tmp += abs(j - s[-1])
        else:
            tmp += min(abs(j - s[s_idx]), abs(j - s[s_idx - 1]))
        ans = min(tmp, ans)
    print(ans)