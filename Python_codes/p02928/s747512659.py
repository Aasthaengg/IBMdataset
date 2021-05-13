n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = pow(10, 9) + 7
numcnt = [0] * 2001
for i in a:
    numcnt[i] += 1
for i in range(1, 2001):
    numcnt[i] += numcnt[i - 1]
ans = 0
for i in range(n):
    cnt = 0
    for j in range(i + 1, n):
        if a[i] > a[j]:
            cnt += 1
    ans += cnt * k
    ans %= mod
    ans += numcnt[a[i] - 1] * (k * (k - 1) // 2)
    ans %= mod
print(ans)