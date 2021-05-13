n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
X=0
Y=0
for i in range(n-1):X=(X+(x[i+1]-x[i])*(i+1)*(n-1-i))%(10**9+7)
for i in range(m-1):Y=(Y+(y[i+1]-y[i])*(i+1)*(m-1-i))%(10**9+7)
print(X*Y%(10**9+7))