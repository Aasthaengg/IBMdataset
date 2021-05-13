x,y = map(int, input().split())
a = 0
b = 0
if x>y:
  while x>y:
    x-=2
    y-=1
    a+=1
if x<y:
  while x<y:
    x-=1
    y-=2
    b+=1
if x == y and x%3==0:
    a+=x//3
    b+=y//3
else:
  print(0)
  exit(0)
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

print(cmb(a+b,b,mod))