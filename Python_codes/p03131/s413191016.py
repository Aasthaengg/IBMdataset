k, a, b = map(int, input().split())

total = 1
cost = b/(a + 1)

if cost > 1:
    if k >= a - 1:
        n = (k - (a - 1)) // 2
        total += n * (b - a)
        total += k - 2 * n
    else:
        total += k
else:
    total += k

print(total)