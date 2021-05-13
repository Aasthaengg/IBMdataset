r, c =map(int, input().split())
data = []
for i in range(r):
    row = list(map(int, input().split()))
    row.append(sum(row))
    data.append(row)

list1 = []
for j in range(c+1):
    temp = 0
    for k in range(r):
        temp += data[k][j]
    list1.append(temp)

for l in data:
    print(*l)
print(*list1)