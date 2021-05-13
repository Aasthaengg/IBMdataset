n, k = map(int, input().split())
p = 0
for i in range(1, n + 1):
    if i < k:
        count = 1
        while (i * (2 ** count)) < k:
            count += 1
        p += (1 / n) * (0.5 ** count)
    else:
        p += 1 / n
print(p)
