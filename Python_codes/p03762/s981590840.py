from itertools import accumulate

n,m=map(int,input().split())
*x,=map(int,input().split())
*y,=map(int,input().split())

acmx=list(accumulate(x))
acmy=list(accumulate(y))
mod=10**9+7
sumx=0
for i in range(n-1):
    sumx+=acmx[n-1]-acmx[i]-(n-i-1)*x[i]
    sumx%=mod

sumy=0
for i in range(m-1):
    sumy+=acmy[m-1]-acmy[i]-(m-i-1)*y[i]
    sumy%=mod

print(sumx*sumy%mod)