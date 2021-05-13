data = []
r, c = [int(n) for n in input().split()]
result = [0 for n in range(c)]

for i in range(r):
    data.append([int(n) for n in input().split()])
    for j in range(c):
        result[j] += data[i][j]
data.append(result)
for i in range(r + 1):
    data[i].append(sum(data[i]))
    print(' '.join([str(n) for n in data[i]]))