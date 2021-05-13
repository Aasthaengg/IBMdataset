r, c = [int(i) for i in input().split()]
array = []

for i in range(r):
    row = [int(i) for i in input().split()]
    row.append(sum(row))
    array.append(row)
    print(*row)

last_array = []
for i in range(c+1):
    total = 0
    for a in array:
        total += a[i]
    last_array.append(total)
print(*last_array)