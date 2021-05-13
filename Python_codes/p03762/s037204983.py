import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
mod = 10**9+7
Xs = list(mapint())
Ys = list(mapint())

xsum = 0
for i in range(N):
    x = Xs[i]
    xsum += (i*x-(N-i-1)*x)
    xsum %= mod
ysum = 0
for i in range(M):
    y = Ys[i]
    ysum += (i*y-(M-i-1)*y)
    ysum %= mod

print(xsum*ysum%mod)