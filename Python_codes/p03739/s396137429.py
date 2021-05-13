import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n = ni()
a = na()

x = 0 #+-+-
y = 0 #-+-+
xx,yy = 0,0

for i in range(n):
    xx += a[i]
    yy += a[i]
    if not i%2:
        p = 0 if xx > 0 else 1-xx
        q = 0 if yy < 0 else 1+yy
        x += p
        y += q
        xx += p
        yy -= q
    else:
        p = 0 if yy > 0 else 1-yy
        q = 0 if xx < 0 else 1+xx
        y += p
        x += q
        yy += p
        xx -= q

print(min(x,y))