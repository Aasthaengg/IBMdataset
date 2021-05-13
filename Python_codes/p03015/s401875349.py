MOD = 10**9+7
T = [1]*(10**5+1)
D = [1]*(10**5+1)
for i in range(10**5):
  T[i+1] = T[i]*3 % MOD
  D[i+1] = D[i]*2 % MOD
L = input()
n = len(L)
ans = 1
count = 0
for i in range(n):
  if L[i] == "1":
    ans += (T[n-1-i]+1)*D[count]
    ans %= MOD
    count += 1
print(ans)