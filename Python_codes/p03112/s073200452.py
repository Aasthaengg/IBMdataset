import bisect
import sys

read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines

a, b, q = map(int, input().split())
s = sorted([int(input()) for _ in range(a)])
t = sorted([int(input()) for _ in range(b)])

for _ in range(q):
    x = int(input())
    s_i = bisect.bisect_left(s, x)
    t_i = bisect.bisect_left(t, x)

    s0, s1, t0, t1 = None, None, None, None
    ans = 10 ** 11
    if s_i > 0:
        s0 = x - s[s_i-1]
    if s_i < a:
        s1 = s[s_i] - x
    if t_i > 0:
        t0 = x - t[t_i-1]
    if t_i < b:
        t1 = t[t_i] - x

    if s0 is not None and t0 is not None:
        ans = min(ans, max(s0, t0))
    if s1 is not None and t1 is not None:
        ans = min(ans, max(s1, t1))
    if s0 is not None and t1 is not None:
        ans = min(ans, s0*2 + t1, t1*2 + s0)
    if s1 is not None and t0 is not None:
        ans = min(ans, s1*2 + t0, t0*2 + s1)

    print(ans)