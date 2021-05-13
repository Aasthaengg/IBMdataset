n, m, c = map(int, input().split())
a = []
b = [int(s) for s in input().split()]
for i in range(n):
    a.append([int(s) for s in input().split()])

count = 0
for i in range(n):
    score = 0
    for j in range(m):
        score += a[i][j] * b[j]
    if score + c > 0:
        count += 1
print(count)