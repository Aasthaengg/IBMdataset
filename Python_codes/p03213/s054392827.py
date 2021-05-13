from collections import defaultdict

def factorization(n):
    if n == 1: return []
    res = []
    x = n
    y = 2
    while y * y <= x:
        while x % y == 0:
            res.append(y)
            x //= y
        y += 1
    if x > 1: res.append(x)
    return res

N = int(input())

D = defaultdict(int)

for i in range(1, N + 1):
    F = factorization(i)
    for f in F:
        D[f] += 1

cnt_75 = 0
cnt_25 = 0
cnt_15 = 0
cnt_5 = 0
cnt_3 = 0

for v in D.values():
    if v + 1 >= 75:
        cnt_75 += 1
    if v + 1 >= 25:
        cnt_25 += 1
    if v + 1 >= 15:
        cnt_15 += 1
    if v + 1 >= 5:
        cnt_5 += 1
    if v + 1 >= 3:
        cnt_3 += 1

ans = 0

ans += cnt_75
ans += cnt_25 * (cnt_3 - 1)
ans += cnt_15 * (cnt_5 - 1)
ans += cnt_5 * (cnt_5 - 1) // 2  * (cnt_3 - 2)

print(ans)