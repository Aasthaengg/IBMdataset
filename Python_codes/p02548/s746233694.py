n = int(input())

table = [0] * (n + 1)

for x in range(1, n + 1):
    for y in range(x, n + 1, x):
        table[y] += 1

res = 0
for c in range(1, n):
    res += table[c]

print(res)