n = int(input())
ans = [0] * n

for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            d = x * x + y * y + z * z + x * y + y * z + z * x
            if d <= n:
                ans[d - 1] += 1

for i in ans:
    print(i)
