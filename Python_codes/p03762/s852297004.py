n,m = map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
area=0
mod=10**9+7

x=0

for i in range(n):
  x += -(n-i-1)*X[i]+i*X[i]

y = 0

for i in range(m):
  y += -(m-i-1)*Y[i]+i*Y[i]

print(x*y%mod)