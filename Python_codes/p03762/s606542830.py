n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
s=0
t=0
p=10**9+7
for i in range(n):
    s=(s-(n-1-2*i)*x[i])%p
for i in range(m):
    t=(t-(m-1-2*i)*y[i])%p
print(s*t%p)
