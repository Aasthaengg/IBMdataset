k = int(input())
s = input()
MOD = 10**9+7

FAC = [1]
INV = [1]
for i in range(1,len(s)+k+1):
  FAC.append((FAC[i-1]*i) % MOD)
  INV.append(pow(FAC[-1],MOD-2,MOD))

def nCr(n,r):
  return FAC[n]*INV[n-r]*INV[r]

p25 = [1]
for i in range(len(s)+k):
  p25.append((p25[-1]*25)%MOD)
p26 = [1]
for i in range(len(s)+k):
  p26.append((p26[-1]*26)%MOD)

ans = 0
for i in range(len(s),len(s)+k+1):
  tmp = nCr(i-1,len(s)-1)*p25[i-len(s)]
  tmp %= MOD
  tmp *= p26[len(s)+k-i]
  tmp %= MOD
  ans +=tmp
  ans %= MOD
print(ans)