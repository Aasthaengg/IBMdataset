a = list(int(input()) for _ in range(5))

min_rem = 10
ans = 0
for i in range(5):
    ans += (a[i] + 10 - 1) // 10 * 10
    if min_rem > a[i] % 10 > 0:
        min_rem = a[i] % 10

if min_rem != 10:
    ans -= (10 - min_rem)
print(ans)