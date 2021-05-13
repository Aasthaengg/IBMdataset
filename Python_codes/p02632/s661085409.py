k=int(input())
s=input()
n=len(s)
mod=pow(10,9)+7

# コンビネーション、さらに高速。あらかじめO(N)の計算をすることでのちの計算が早くなる
def cmb(n,r,mod):
  if (r<0 or r>n):
    return 0
  r=min(r,n-r)
  return g1[n]*g2[r]*g2[n-r]%mod
g1=[1,1] 
g2=[1,1] 
inverse=[0,1]
for i in range(2,n+k+1):
  g1.append((g1[-1]*i)%mod)
  inverse.append((-inverse[mod%i]*(mod//i))%mod)
  g2.append((g2[-1]*inverse[-1])%mod)

f=[pow(25,i,mod)*cmb(i+n-1,n-1,mod) for i in range(k+1)]
g=[0]*(k+1)
g[0]=1
for ki in range(1,k+1):
  g[ki]=f[ki]+26*g[ki-1]
  g[ki]%=mod
print(g[k])
