mod=10**9+7
n,m=map(int,input().split())
X=list(map(int,input().split()))
Y=list(map(int,input().split()))
p=0
q=0
for i in range(n-1):
    p=(p+(X[i+1]-X[i])*(i+1)%mod*(n-i-1))%mod
for i in range(m-1):
    q=(q+(Y[i+1]-Y[i])*(i+1)%mod*(m-i-1))%mod
print(p*q%mod)