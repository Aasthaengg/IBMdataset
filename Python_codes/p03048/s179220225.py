r, g, b, n = [int(i) for i in input().split()]
t1 = n // r + 1
t2 = n // g + 1
ans = 0
for i in range(t1):
    for j in range(t2):
        t = r * i + g * j
        if (n - t) >= 0 and (n - t) % b == 0: ans += 1
print(ans)
