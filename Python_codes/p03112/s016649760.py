import sys
input = sys.stdin.readline
from bisect import *

A, B, Q = map(int, input().split())
s = [-10**18]+[int(input()) for _ in range(A)]+[10**18]
t = [-10**18]+[int(input()) for _ in range(B)]+[10**18]

for _ in range(Q):
    x = int(input())
    i = bisect_left(s, x)
    sl = s[i-1]
    sr = s[i]
    i = bisect_left(t, x)
    tl = t[i-1]
    tr = t[i]
    ans = 10**18
    
    for fi in [sl, sr]:
        for se in [tl, tr]:
            ans = min(ans, abs(fi-x)+abs(se-fi))
    
    for fi in [tl, tr]:
        for se in [sl, sr]:
            ans = min(ans, abs(fi-x)+abs(se-fi))
    
    print(ans)