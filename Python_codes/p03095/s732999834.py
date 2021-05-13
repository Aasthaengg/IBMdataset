from collections import Counter

N = int(input())
S = list(input())
C = Counter(S)
MOD = 10 ** 9 + 7

ans = 1
for s,c in C.items():
  ans *= c + 1
  ans %= MOD

ans = (ans - 1) % MOD
print(ans)



