import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


a,b,q = list(map(int, input().split()))
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
from bisect import bisect_left as bl
ls = [None]*a
lt = [None]*b
for i in range(a):
    ind = bl(t, s[i])
    v = float("inf")
    if ind<b:
        v = min(v, abs(t[ind]-s[i]))
    if ind>0:
        v = min(v, abs(t[ind-1]-s[i]))
    ls[i] = v
for i in range(b):
    ind = bl(s, t[i])
    v = float("inf")
    if ind<a:
        v = min(v, abs(s[ind]-t[i]))
    if ind>0:
        v = min(v, abs(s[ind-1]-t[i]))
    lt[i] = v
ans = [None]*q
for i in range(q):
    x = int(input())
    v = float("inf")
    ind = bl(s, x)
    if ind<a:
        v = min(v, abs(s[ind]-x)+ls[ind])
    if ind>0:
        v = min(v, abs(s[ind-1]-x)+ls[ind-1])
    ind = bl(t, x)
    if ind<b:
        v = min(v, abs(t[ind]-x)+lt[ind])
    if ind>0:
        v = min(v, abs(t[ind-1]-x)+lt[ind-1])
    ans[i] = v
write("\n".join(map(str, ans)))