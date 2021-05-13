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

DIV=10**9+7

def cmb(n, r, DIV):
  if ( r<0 or r>n ):
    return 0
  r = min(r, n-r)
  return g1[n] * g2[r] * g2[n-r] % DIV

P = 10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, P + 1 ):
  g1.append( ( g1[-1] * i ) % DIV )
  inverse.append( ( -inverse[DIV % i] * (DIV//i) ) % DIV )
  g2.append( (g2[-1] * inverse[-1]) % DIV )

N,M=map(int,input().split())
if M==1:
  print(1)
  exit(0)
facs=factorization(M)
ans=1
for fac in facs:
  a,b=fac[0],fac[1]
  # 区別しないb個のモノを区別可能なN個の箱に分ける（0個の箱があってもよい）
  # (b+(N+1)) C b
  ans=((ans%DIV)*(cmb(b+(N-1),b,DIV))%DIV)%DIV

print(ans)
