n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
mod=10**9+7
h=[]
for i in range(n):
    h.append(x[i]-x[0])
x=h
h=[]
for i in range(m):
    h.append(y[i]-y[0])
y=h

s=0
for i in range(n):
    s=(s+x[i])%mod
t=0
for i in range(m):
    t=(t+y[i])%mod

data=[s]
for i in range(1,n):
    u=data[-1]-(x[i]-x[i-1])*(n-i)
    data.append(u)
s=0
for v in data:
    s=(s+v)%mod
data=[t]
for i in range(1,m):
    u=data[-1]-(y[i]-y[i-1])*(m-i)
    data.append(u)
t=0
for v in data:
    t=(t+v)%mod

print(s*t%mod)