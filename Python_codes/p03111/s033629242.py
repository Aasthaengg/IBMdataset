from itertools import combinations


n, a, b, c = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))

dp_a = [-1] * (2 ** n)
dp_b = [-1] * (2 ** n)
dp_c = [-1] * (2 ** n)

for i in range(1, n-1):
    for j in combinations(range(n), i):
        indices = [1 << k for k in j]
        index = sum(indices)
        if i == 1:
            dp_a[index] = abs(l[j[0]] - a)
            dp_b[index] = abs(l[j[0]] - b)
            dp_c[index] = abs(l[j[0]] - c)
        else:
            dp_a[index] = min([dp_a[index - indices[k]] for k in range(i)])
            dp_a[index] = min(dp_a[index], abs(sum([l[k] for k in j]) - a) + 10 * (i-1))

            dp_b[index] = min([dp_b[index - indices[k]] for k in range(i)])
            dp_b[index] = min(dp_b[index], abs(sum([l[k] for k in j]) - b) + 10 * (i - 1))

            dp_c[index] = min([dp_c[index - indices[k]] for k in range(i)])
            dp_c[index] = min(dp_c[index], abs(sum([l[k] for k in j]) - c) + 10 * (i - 1))

ans = 10 ** 10
for i in range(1, 2 ** n):
    for j in range(1, 2 ** n):
        if i | j != i + j:
            continue
        for k in range(1, 2 ** n):
            if i + j + k == 2 ** n - 1 and i | j | k == 2 ** n - 1:
                ans = min(ans, dp_a[i] + dp_b[j] + dp_c[k])

print(ans)