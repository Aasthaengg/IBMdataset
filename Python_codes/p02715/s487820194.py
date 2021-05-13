mod = 10 ** 9 + 7
n, k = map(int, input().split())

a = [1] * (k+1)
b = [ i for i in range(k+1) ]

for i in range(k//2,0,-1):
  cnt = pow( k // i , n, mod )
  for j in range(i*2,k+1,i):
    cnt = ( cnt - a[j] ) % mod
  a[i] = cnt
  b[i] = i * cnt % mod

ans = 0
for i in range(1,k+1):
  ans += b[i]
  if ans >= mod:
    ans %= mod

print(ans)