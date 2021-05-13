n = int(input())
a = list(map(int, input().split()))

mod = 10 ** 9 + 7

res = 0
two_factor = 1
for i in range(60):
    cnt_1 = 0
    cnt_0 = 0
    for v in a:
        if (v >> i) & 1:
            cnt_1 += 1
        else:
            cnt_0 += 1
    res = (res + cnt_1 * cnt_0 % mod * two_factor % mod) % mod
    two_factor = two_factor * 2 % mod

print(res)