N, K = map(int, input().split())
gcd_list = [0] * K#K, K-1, K-2の順
MOD = 10 ** 9 + 7

for i in range(K, 0, -1):
  #print(i)
  ans2 = pow((K // i), N, MOD)#
  x = i
  while x <= K:
    ans2 -= gcd_list[K - x]
    x += i
  gcd_list[K - i] = ans2 % MOD
  
ans = 0  
for i in range(K):
  ans += (gcd_list[i] * (K - i)) % MOD
  
print(ans % MOD)