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
def cmb(n, r, mod):
   if ( r<0 or r>n ):
       return 0
   r = min(r, n-r)
   return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**5+100
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
   g1.append( ( g1[-1] * i ) % mod )
   inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
   g2.append( (g2[-1] * inverse[-1]) % mod )
N,M=map(int,input().split())
A=factorization(M)
ans=1
if M==1:
 print(1)
else:
 for i in range(len(A)):
  ans*=cmb(N+A[i][1]-1, N-1, mod)
  ans%=(10**9+7)
 print(ans)