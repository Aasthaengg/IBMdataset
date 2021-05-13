M=10**9+7
n,k=map(int,input().split())
for i in range(k):
  if n-k<i: print(0)
  else:
    s=t=1
    for j in range(1,i+1): s=s*(n-k+2-j)*(k-j)%M; t=t*j*j%M
    print(s*(n-k+1-i)*pow(t*(i+1),M-2,M)%M)