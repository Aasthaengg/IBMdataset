n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    cnt1 = 0
    cnt2 = 0
    for j in range(n):
        if j <= i and a[i] > a[j]:
            cnt1 += 1
        elif j > i and a[i] > a[j]:
            cnt2 += 1
    ans += ((cnt2 * k) + ((cnt1 + cnt2) * k * (k - 1) // 2)) % (10 ** 9 + 7)
print(ans % (10 ** 9 + 7))
