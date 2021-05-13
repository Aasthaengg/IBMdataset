import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n = ni()
p = na()
ans = 0

for i in range(n-1):
    j = i+1
    if j == p[i]:
        p[i],p[i+1] = p[i+1],p[i]
        ans += 1
if p[-1] == n:
    ans += 1
print(ans)