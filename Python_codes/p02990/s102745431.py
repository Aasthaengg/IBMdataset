m = 10**9+7
def nCr(n,r):
  if r*2>n:
      return nCr(n,n-r)
  else:
      a = b = 1
      for i in range(r):
          a = a * (n - i) % m
          b = b * (r - i) % m
      return (a * pow(b,m-2,m)) % m

n,k=map(int,input().split())
for i in range(k):
    if n-k+1>=i+1:
        print((nCr(n-k+1,i+1)%m)*(nCr(k-1,k-1-i)%m)%m)
    else:
        print(0)