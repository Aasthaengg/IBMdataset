n,m=map(int,input().split())
X=list(map(int,input().split()))
Y=list(map(int,input().split()))
x=[]
MOD=10**9+7
for i in range(n-1):
    x.append(X[i+1]-X[i])
y=[]
for i in range(m-1):
    y.append(Y[i+1]-Y[i])
xlen=0
for i in range(n-1):
    xlen+=((i+1)*((n-i-1)*x[i])%MOD)%MOD
ylen=0
for j in range(m-1):
    ylen+=(((j+1)*((m-j-1)*y[j])%MOD)%MOD)
print((xlen*ylen)%MOD)
