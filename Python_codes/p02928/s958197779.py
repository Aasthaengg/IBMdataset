N, K = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
mod = 10 ** 9 + 7
for i in range(N):
    #print(cnt)
    for j in range(N):
        if a[i] > a[j]:
            cnt += 1
ans = cnt * ((K - 1) * K) * 500000004 % mod
for i in range(N - 1):
    for j in range(i + 1, N):
        if a[i] > a[j]:
            ans += K % mod
print(ans % mod)