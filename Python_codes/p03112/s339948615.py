from bisect import bisect
import sys
input = sys.stdin.readline

A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
s.sort()
t = [int(input()) for _ in range(B)]
t.sort()
for _ in range(Q):
    x = int(input())
    i = bisect(s, x)
    sl = sr = 0
    if i == 0:
        sl = -float('inf')
        sr = s[i]
    elif i == A:
        sl = s[i-1]
        sr = float('inf')
    else:
        sl = s[i-1]
        sr = s[i]
    j = bisect(t, x)
    tl = tr = 0
    if j == 0:
        tl = -float('inf')
        tr = t[j]
    elif j == B:
        tl = t[j-1]
        tr = float('inf')
    else:
        tl = t[j-1]
        tr = t[j]
    ans = min(max(sr, tr)-x, x-min(sl, tl), x+sr-2*tl, x+tr-2*sl, 2*sr-x-tl, 2*tr-x-sl)
    print(ans)
