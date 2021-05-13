R=range
M=998244353
n,m,k=map(int,input().split())
f=1
for i in R(n-1):f=f*-~i%M
r=[pow(f*n,-1,M)]
for i in R(n):r+=r[i]*(n-i)%M,
print(sum(m*f*r[i-n]*r[~i]*pow(m-1,~i+n,M)for i in R(k+1))%M)