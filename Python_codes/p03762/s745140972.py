n,m = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x.sort()
y.sort()
N = 10**9+7
Lx=0
Ly=0
for i in range(n):
    Lx += (-n+2*i+1)*x[i]
    Lx %= N
for i in range(m):
    Ly += (-m+2*i+1)*y[i]
    Ly %= N
ans = Lx*Ly%N
print(ans)