import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

n,m = MI()
x,y = LI(),LI()
mod = 10**9+7

n,m = n-1,m-1
dx = [x[i+1]-x[i] for i in range(n)]
dy = [y[i+1]-y[i] for i in range(m)]

if n % 2 == 0:
    rx = [i*(n+1-i) for i in range(1,n//2+1)] + [i*(n+1-i) for i in range(n//2,0,-1)]
else:
    rx = [i*(n+1-i) for i in range(1,n//2+2)] + [i*(n+1-i) for i in range(n//2,0,-1)]
if m % 2 == 0:
    ry = [i*(m+1-i) for i in range(1,m//2+1)] + [i*(m+1-i) for i in range(m//2,0,-1)]
else:
    ry = [i*(m+1-i) for i in range(1,m//2+2)] + [i*(m+1-i) for i in range(m//2,0,-1)]

a = 0
for i,j in zip(dx,rx):
    a += i*j
    a %= mod
b = 0
for i,j in zip(dy,ry):
    b += i*j
    b %= mod

print((a*b) % mod)
