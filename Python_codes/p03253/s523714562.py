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
  if ( r < 0 or r > n ):
    return 0
  r = min(r, n - r)
  return g1[n] * g2[r] * g2[n - r] % mod
 
MOD = 10 ** 9 + 7
SIZE = 10 ** 5 * 2 + 1
g1 = [1, 1]
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル
 
for i in range(2, SIZE + 1 ):
  g1.append((g1[-1] * i) % MOD)
  inverse.append((-inverse[MOD % i] * (MOD // i) ) % MOD)
  g2.append((g2[-1] * inverse[-1]) % MOD)

N, M = map(int, input().split())

if M == 1:
  print(1)
  exit()

answer = 1
for p, a in factorization(M):
  answer = (answer * cmb(N - 1 + a, a, MOD)) % MOD

print(answer)