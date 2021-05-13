N, K = map(int, input().split())
mod = 10 ** 9 + 7
ans = 0

for i in range(K,N+2):
    a = i * (N + 1 - i) + 1
    a %= mod
    ans += a
    ans %= mod

print(ans) 