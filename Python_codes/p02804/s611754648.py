M=10**9+7
f=lambda:map(int,input().split())
n,k=f()
l=sorted(f())
c,a=1,l[k-1]-l[-k]
for i in range(k,n):
  c=c*i*pow(i-k+1,M-2,M)%M
  a+=c*(l[i]-l[~i])%M
print(a%M)