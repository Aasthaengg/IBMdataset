import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n = ni()
a,b = na()
p = na()
c = [0,0,0]

for i in p:
    if i <= a:
        c[0] += 1
    elif a+1 <= i <= b:
        c[1] += 1
    else:
        c[2] += 1

print(min(c))