
N, K = map(int, input().split())

MOD = 10 ** 9 + 7
count = [0] * (N + 1)
for i in range(1, N + 1):
    count[i] += count[i - 1] + i
    count[i] %= MOD

ans = 1
for k in range(K, N + 1):
    ans += count[-1] - count[-k - 1] - count[k - 1] + 1
    ans %= MOD
print(ans)
