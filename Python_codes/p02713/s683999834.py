
k = int(input())

gcd_cnt = {}

for n in range(k, 0, -1):
    div_all = (k // n) ** 3
    div_dup = 0
    for m in range(n * 2, k + 1, n):
        div_dup += gcd_cnt[m]
    gcd_cnt[n] = div_all - div_dup

ans = 0
for gcd in gcd_cnt.keys():
    ans += gcd * gcd_cnt[gcd]

print(ans)
