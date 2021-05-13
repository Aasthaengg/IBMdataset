mod = 10**9 + 7
def binomial_coefficients(n, k):
  if k==0 or k==n:
    return 1
  modinv_table = [-1] * (k+1)
  modinv_table[1] = 1
  for i in range(2, k+1):
    modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod
  ans = 1
  for i in range(k):
    ans *= n-i
    ans *= modinv_table[i + 1]
    ans %= mod
  return ans

N,K=map(int,input().split())
R=N-K
for i in range(1,K+1):
  if R<i-1:
    print(0)
  else:
    r=binomial_coefficients(R+1, i)
    b=binomial_coefficients(K-1, i-1)
    print((r*b)%1000000007)