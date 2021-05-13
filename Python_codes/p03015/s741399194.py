MOD = 10**9 + 7
L = input()[1:]

ans = [2, 1]
for l in L:
  ans[1] *= 3
  ans[1] %= MOD
  if l == '1':
    ans[1] += ans[0]
    ans[0] *= 2
    ans[0] %= MOD

print(sum(ans) % MOD)