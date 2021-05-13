import sys
import bisect
input = sys.stdin.readline
A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
s = sorted(s)
t = sorted(t)

for _ in range(Q):
    x = int(input())
    idx1 = bisect.bisect_right(s, x)
    idx2 = bisect.bisect_right(t, x)
    ans = float('inf')
    if idx1 > 0:
        left_s = s[idx1-1]
    else:
        left_s = float('inf')
    if idx2 > 0:
        left_t = t[idx2-1]
    else:
        left_t = float('inf')
    if idx1 < A:
        right_s = s[idx1]
    else:
        right_s = float('inf')
    if idx2 < B:
        right_t = t[idx2]
    else:
        right_t = float('inf')

    ls = x-left_s
    lt = x-left_t
    rs = right_s-x
    rt = right_t-x 
    if left_s <= x <= right_t:
        tmp = right_t-left_s + min(ls, rt)
        ans = min(ans, tmp)
    if left_t <= x <= right_s:
        tmp = right_s-left_t + min(lt, rs)
        ans = min(ans, tmp)
    ans = min(ans, max(abs(ls), abs(lt)))
    ans = min(ans, max(abs(rs), abs(rt)))
    print(ans)
