import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m = list(map(int, input().split()))
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))
vx = 0
vy = 0
M  = 10**9+7
for i in range(n-1):
    vx += (xs[i+1]-xs[i]) * (i+1) * (n-i-1)
    vx %= M
for i in range(m-1):
    vy += (ys[i+1]-ys[i]) * (i+1) * (m-i-1)
    vy %= M
ans = (vx*vy)%M
print(ans%M)