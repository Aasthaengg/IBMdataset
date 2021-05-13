N, K = map(int, input().split())
mod_0 = 0
mod_K2 = 0
for i in range(1, N+1):
  if i % K == 0:
    mod_0 += 1
  elif i % K == K/2:
    mod_K2 += 1

ans = pow(mod_0, 3) + pow(mod_K2, 3)
print(ans)