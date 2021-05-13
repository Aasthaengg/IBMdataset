n,m = map(int,input().split())

MOD = 10**9 + 7
FAC = [1]
INV = [1]
for i in range(1,max(m,n)+1):
  FAC.append((FAC[i-1]*i) % MOD)
  INV.append(pow(FAC[-1],MOD-2,MOD))

def nPr(n,r):
  return FAC[n]*INV[n-r]

if abs(n-m) > 1:
  print(0)
else:
  ans = nPr(n,n)*nPr(m,m)
  ans %= MOD
  if n == m:
    ans *= 2
    ans %= MOD
  print(ans)