import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n,t = na()
a = na()
b = [0]
c = a[0]
for i in range(1,n):
    b.append(a[i]-c)
    c = min(c,a[i])

print(b.count(max(b)))