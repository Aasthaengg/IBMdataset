MOD=10**9+7
n,m=map(int,input().split())
x=sorted(map(int,input().split()))
y=sorted(map(int,input().split()))
X,Y=0,0
for i in range(n):
    X=X+x[i]*(i+1)%MOD
    X=(X-x[i]*(n-i)+MOD)%MOD
for k in range(m):
    Y=Y+y[k]*(k+1)%MOD
    Y=(Y-y[k]*(m-k)%MOD+MOD)%MOD
print(X*Y%MOD)