n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    a.append([int(s) for s in input().split()])
for j in range(m):
    b.append([int(input())])

for x in range(n):
    sum = 0
    for y in range(m):
        sum += a[x][y] * b[y][0]
    print(sum)