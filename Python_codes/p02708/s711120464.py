def sum_of(n):
    return n * (n - 1) // 2

N, K = map(int, input().split())
mod = 10**9 + 7
ans = 0

for i in range(K, N + 2):
    mini = sum_of(i)
    maxi = sum_of(N + 1) - sum_of(N - i + 1)
    ans += (maxi - mini + 1)

print(ans % mod)