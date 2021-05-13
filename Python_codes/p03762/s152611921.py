n,m = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x = [x[i+1]-x[i] for i in range(n-1)]
y = [y[i+1]-y[i] for i in range(m-1)]
mod = 10**9+7
sumx = 0
sumy = 0
for i in range(n-1):
    sumx += x[i]*(i+1)*(n-1-i)%mod
for i in range(m-1):
    sumy += y[i]*(i+1)*(m-1-i)%mod
print(sumx*sumy%mod)