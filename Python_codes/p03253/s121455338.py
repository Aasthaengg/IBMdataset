from math import sqrt,floor
def comb(n,m):
  if m == 0:
    return 1
  return comb(n-1,m-1)*n // m
n,m=map(int,input().split())
mod=10**9+7
def factorization(x):
  ans=[]
  for i in range(2,floor(sqrt(x))+1):
    if x%i==0:
      cnt=0
      while x%i==0:
        x//=i
        cnt+=1
      ans.append([i,cnt])
      if x==1:
        break
  if x!=1:
    ans.append([x,1])
  return ans
g=factorization(m)
ans=1
for i in g:
  ans=(ans*(comb(i[1]+n-1,i[1])%mod))%mod
print(ans)