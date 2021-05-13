n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
X=[]
Y=[]
for i in range(n-1):
  X.append(x[i+1]-x[i])
for i in range(m-1):
  Y.append(y[i+1]-y[i])
for i in range(n-1):
  X[i]=X[i]*(n-i-1)*(i+1)%(10**9+7)
for i in range(m-1):
  Y[i]=Y[i]*(m-i-1)*(i+1)%(10**9+7)
print((sum(X)%(10**9+7)*sum(Y)%(10**9+7))%(10**9+7))