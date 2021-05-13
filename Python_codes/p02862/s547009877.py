x, y = map(int, input().split())
mod = 10 ** 9 + 7

cnt1 = cnt2 = 0
for i in range(x + 1):
    x_left = x - i
    y_left = y - 2 * i
    if x_left == y_left * 2:
        cnt1 = i
        cnt2 = y_left

if cnt1 == cnt2 == 0:
    ans = 0
else:
    ans = 1
    for i in range(1, cnt1 + 1):
        ans *= (cnt1 + cnt2 - i + 1)
        ans %= mod
        ans *= pow(i, mod - 2, mod)
        ans %= mod

print(ans)
