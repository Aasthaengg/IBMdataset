n,k=map(int,input().split())
MOD=10**9+7
def comb(n,m,p=10**9+7):
    buf=perm[n]*inv[m]
    buf%=MOD
    buf*=inv[n-m]
    buf%=MOD
    return buf
def inv_mod(a):
  return pow(a,MOD-2,MOD)

perm=[1]*(2*n+1)
for i in range(1,2*n+1):
    perm[i]=perm[i-1]*(i)
    perm[i]%=MOD
inv=[1]*(2*n+1)
inv[-1]=inv_mod(perm[-1])
for i in range(2*n-1,-1,-1):
    inv[i]=inv[i+1]*(i+1)
    inv[i]%=MOD
#print(comb(5,2))
buf=comb(2*n-1,n)
for j in range(k+1,n):
    x=comb(n,j)*comb(n-1,j)
    x%=MOD
    buf-=x
    buf%=MOD
print(buf)