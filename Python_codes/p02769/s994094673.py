U = 5*10**5
MOD = 10**9+7
 
def main():
  fact = [1]*(U+1)
  fact_inv = [1]*(U+1)

  for i in range(1,U+1):
      fact[i] = (fact[i-1]*i)%MOD
  fact_inv[U] = pow(fact[U], MOD-2, MOD)

  for i in range(U,0,-1):
      fact_inv[i-1] = (fact_inv[i]*i)%MOD

  def comb(n, k):
      if k < 0 or k > n:
          return 0
      z = fact[n]
      z *= fact_inv[k]
      z *= fact_inv[n-k]
      z %= MOD
      return z

  n, k = map(int, input().split())
  if k+1 < n:
    ans = 0
    for i in range(k+1, n):
      ans += comb(n, i) * comb(n-1, i)
      ans %= MOD
    ans = comb(2*n-1, n) - ans
    ans %= MOD
  else:
    ans = comb(2*n-1, n)
  print(ans)
  
if __name__ == "__main__":
  main()