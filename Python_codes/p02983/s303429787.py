l, r = map(int, input().split())

ans = 2020
for i in range(l, l + 2019):
    for j in range(i + 1, i + 2020):
        if j <= r:
            ans = min(ans, (i*j) % 2019)
print(ans)
