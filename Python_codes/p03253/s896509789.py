n,m=map(int,input().split())
mod=10**9+7


# コンビネーション、さらに高速。あらかじめO(N)の計算をすることでのちの計算が早くなる
def cmb(n,r,mod):
  if (r<0 or r>n):
    return 0
  r=min(r,n-r)
  return g1[n]*g2[r]*g2[n-r]%mod
g1=[1,1] # g1[i]=i! % mod　:階乗
g2=[1,1] # g2[i]=(i!)^(-1) % mod　:階乗の逆元
inverse=[0,1]
for i in range(2,min(2*10**5,n+m)+1):
  g1.append((g1[-1]*i)%mod)
  inverse.append((-inverse[mod%i]*(mod//i))%mod)
  g2.append((g2[-1]*inverse[-1])%mod)

#heap

def factorization(n):
  arr = []
  temp = n
  for i in range(2, int(-(-n**0.5//1))+1):
    if temp%i==0:
      cnt=0
      while temp%i==0:
        cnt+=1
        temp //= i
      arr.append([i, cnt])
  if temp!=1:
    arr.append([temp, 1])
  if arr==[]:
    arr.append([n, 1])
  return arr
#factorization(24) 
## [[2, 3], [3, 1]] 
##  24 = 2^3 * 3^1

if m==1:
  print(1)
  exit()
ary=factorization(m)
ans=1
for x,y in ary:
  ans*=cmb(n-1+y,y,mod)
  ans%=mod
print(ans)