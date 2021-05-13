n, k = map(int, input().split())

max_alpha = 2 * n // k
if k % 2 == 0:
    if max_alpha % 2 == 0:
        ans = 2 * ((max_alpha / 2) ** 3)
    else:
        ans = ((max_alpha + 1) /2) ** 3 + ((max_alpha - 1) /2) ** 3
else:
    ans = (max_alpha // 2) ** 3
print(int(ans))
