n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = int(1e9 + 7)
cnt_a = [0] * 2005
for i in a:
    cnt_a[i] += 1
less = 0
m = 0
for i in cnt_a:
    if i == 0:
        continue
    m += less * i
    less += i
ans = 0
for i in range(n):
    cnt = 0
    for j in range(i):
        if a[j] > a[i]:
            cnt += 1
    ans += cnt * k % mod
ans += m * k * (k - 1) // 2 % mod
print(ans % mod)