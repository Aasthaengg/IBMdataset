import numpy as np
U = 10**5
T = np.zeros(U,np.int32)
T[2] = 1
T[3::2] = 1
for i in range(U):
  if i*i>U:
    break
  if T[i]:
    T[i*i::2*i] = 0
pls = np.where(T)[0]
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
    
N, M = map(int, input().split())
dic = {}
for p in pls:
  cnt = 0
  while M%p==0:
    M //= p
    cnt += 1
  dic[p] = cnt
if M!=1:
  dic[M] = 1
ans = 1
for k in dic.keys():
  ans *= cmb(dic[k]+N-1,N-1,mod)
  ans %= mod
print(ans)