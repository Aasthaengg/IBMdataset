
def pre_combi1(n, p):
  fact = [1]*(n+1)  # fact[n] = (n! mod p)
  factinv = [1]*(n+1)  # factinv[n] = ((n!)^(-1) mod p)
  inv = [0]*(n+1)  # factinv 計算用
  inv[1] = 1
  # 前処理
  for i in range(2, n + 1):
    fact[i]= fact[i-1] * i % p
    inv[i]= - inv[p % i] * (p // i) % p
    factinv[i]= factinv[i-1] * inv[i] % p
  return fact, factinv

def combi1(n, r, p, fact, factinv):
  """
  k<n<10**7でpが素数のときのnCr % pを求める
   """
  # 本処理
  if r < 0 or n < r:
    return 0
  r = min(r, n-r)
  return fact[n] * factinv[r] * factinv[n-r] % p
 
n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
sfs=0
p=1000000007
fact,factinv=pre_combi1(n,p)
for i in range(1,n+1):
  sfs+=a[i-1]*combi1(i-1,k-1,p,fact,factinv)
  sfs-=a[i-1]*combi1(n-i,k-1,p,fact,factinv)
  sfs %= p
  #print(i,a[i-1],n-i,k-1,sfs)
print(sfs%p)