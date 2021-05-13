import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline

n = int(input())

ls = []; rs = []
for _ in range(n):
    a,b = [int(i) for i in readline().split()]
    ls.append(a)
    rs.append(b)

ls.sort()
rs.sort()

ans = 0

if n%2 == 1:
    l = ls[n//2]
    r = rs[n//2]
    ans = r-l+1
else:
    l2 = ls[n//2-1]+ls[n//2]
    r2 = rs[n//2-1]+rs[n//2]
    ans = r2-l2+1

print(ans)