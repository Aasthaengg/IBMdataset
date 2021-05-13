n = int(input())

ans = [0 for _ in range(10001)]

for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            f = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if f < 10001:
                ans[f-1] += 1

for i in range(n):
    print(ans[i])