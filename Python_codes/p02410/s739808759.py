N = [int(i) for i in input().split()]

result = [0 for _ in range(N[0])]
row = []
col = []
for num, info in enumerate(range(N[0]+N[1])):
    if num < N[0]:
        row.append([int(i) for i in input().split()])
    else:
        col.append(int(input()))

for num, r in enumerate(row):
    res = 0
    for i, j in zip(r, col):
        res += i * j
    result[num] = res

for i in result:
    print(str(i))
