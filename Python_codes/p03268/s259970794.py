N, K = map(int, input().split())
mod_is_0 = 0
mod_is_half_K = 0
for i in range(1, N+1):
    if i%K == 0:
        mod_is_0 += 1
    if K%2 == 0 and i%K == K/2:
        mod_is_half_K += 1
print(mod_is_0**3+mod_is_half_K**3)