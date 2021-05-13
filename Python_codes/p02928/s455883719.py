MOD = 10 ** 9 + 7

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    cnt1 = 0
    cnt2 = 0
    for j in range(n):
        if i == j:
            continue
        if a[i] > a[j]:
            if i < j:
                cnt1 += 1
            else:
                cnt2 += 1
    ans += cnt1 * (k * (k + 1) // 2) + cnt2 * ((k - 1) * k // 2)
    ans %= MOD
print(ans)