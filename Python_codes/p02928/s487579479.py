N, K = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
two = (-1 * (mod//2)) % mod
cnt = 0
for i in range(N):
    for j in range(N):
        if a[i] > a[j]:
            cnt += 1
ans = cnt * (K - 1) * K * two % mod
for i in range(N - 1):
    for j in range(i + 1, N):
        if a[i] > a[j]:
            ans += K
print(ans % mod)