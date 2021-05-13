def change_n_shinsu(x, n):
    ans = ''
    while True:
        shou = x // n
        amari = x % n
        if shou == 0 and amari == 0:
            break
        ans = str(amari) + ans
        x = shou
    ans = ans.zfill(60)
    return ans

n = int(input())
a = list(map(int, input().split()))
mod = 10**9+7

zero = [0 for i in range(60)]
one = [0 for i in range(60)]

for i in range(n):
    ai = change_n_shinsu(a[i], 2)
    for j in range(60):
        if ai[j] == '0':
            zero[j] += 1
        else:
            one[j] += 1

zero = zero[::-1]
one = one[::-1]

ans = 0
for i in range(60):
    kumi = (zero[i] * one[i]) % mod
    num = pow(2, i, mod)
    ans += (kumi * num) % mod
    ans %= mod
print(ans)