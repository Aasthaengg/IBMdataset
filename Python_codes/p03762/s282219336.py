#058-D
n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
sx=0
sy=0
for i in range(n):
    sx+=i*x[i]-(n-i-1)*x[i]
for i in range(m):
    sy+=i*y[i]-(m-i-1)*y[i]
sx=sx%(10**9+7)
sy=sy%(10**9+7)
ans=sx*sy%(10**9+7)
print(ans)