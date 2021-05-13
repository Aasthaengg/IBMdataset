import sys
input = sys.stdin.readline
from bisect import *

A, B, Q = map(int, input().split())
s = [-10**18]+[int(input()) for _ in range(A)]+[10**18]
t = [-10**18]+[int(input()) for _ in range(B)]+[10**18]

for _ in range(Q):
    x = int(input())
    idx1 = bisect_right(s, x)
    idx2 = bisect_right(t, x)
    ls, rs = s[idx1-1], s[idx1]
    lt, rt = t[idx2-1], t[idx2]
    ans = 10**18
    
    for p1, p2 in [(ls, lt), (ls, rt), (rs, lt), (rs, rt), (lt, ls), (lt, rs), (rt, ls), (rt, rs)]:
        ans = min(ans, abs(p1-x)+abs(p2-p1))
    
    print(ans)