r, g, b, n = map(int, input().split())
ans = 0
for i in range(n + 1):
    total = i * r
    if total > n:
        break
    for j in range(n + 1):
        total2 = total + j * g
        if total2 > n:
            break
        b_cnt = n - total2
        if b_cnt % b == 0:
            ans += 1
print(ans)