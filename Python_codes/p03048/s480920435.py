r, g, b, n = map(int, input().split())

ans = 0
r_p = n // r
for i in range(n // r + 1):
    tmp = n - r * i
    for j in range(tmp // g + 1):
        remain = tmp - g * j
        if remain % b == 0:
            ans += 1
print(ans)
