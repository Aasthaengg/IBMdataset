n = int(input())

table = {}

for num in range(1, n + 1):
    l = num % 10
    tmp = num
    while tmp >= 10:
        tmp //= 10
    m = tmp % 10

    if (l, m) not in table:
        table[(l, m)] = 1
    else:
        table[(l, m)] += 1

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        if (i, j) in table and (j, i) in table:
            ans += table[(i, j)] * table[(j, i)]

print(ans)
