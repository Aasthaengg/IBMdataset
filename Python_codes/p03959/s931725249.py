import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n = ni()
t = na()
a = na()
mod = 10**9+7

ans = 1
for i in range(n):
    tt,aa = 1,1
    if i == 0 or t[i-1] < t[i]:
        tt = t[i]
    if i == n-1 or a[i+1] < a[i]:
        aa = a[i]
    if tt > a[i] or aa > t[i]:
        print(0)
        exit()
    p = min(t[i],a[i]) - max(tt,aa) + 1
    ans = ans*p%mod

print(ans)