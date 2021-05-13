n,m=map(int,input().split())
d=dict()
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**6+10
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
for i in range(1,int(m**0.5)+1):
  cnt=0
  while m%(i+1)==0:
    cnt+=1
    m//=(i+1)
  if cnt>0:
    if i+1 not in d:
      d[i+1]=cnt
    else:
      d[i+1]+=cnt
if m>1:
  if m not in d:
    d[m]=1
  else:
    d[m]+=1
d=list(d.items())
ans=1
for p,root in d:
  ans*=cmb(root+n-1,n-1,mod)
  ans%=mod
print(ans%mod)