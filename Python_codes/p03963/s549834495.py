def combination(n, r):
    res_n = 1
    res_r = 1

    for _ in range(r):
        res_n *= n
        n -= 1

    for _ in range(r):
        res_r *= r
        r += 1

    return res_n // res_r

n, k = map(int, input().split(" "))

res = 0
for i in range(n):
    if i == 0:
        res = combination(k, 1)
    else:
        res *= combination(k - 1, 1)

print(res)