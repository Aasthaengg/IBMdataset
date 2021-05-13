table = [1, ]
for i in range(2, 1000):
    table.append(table[i-2] + i)

a, b = map(int, input().split())
print(table[b-a-1] - b)