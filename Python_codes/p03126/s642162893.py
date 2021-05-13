n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
l = [0] * m
for i in range(n):
    for j in range(m):
        if j + 1 in a[i][1:]:
            l[j] += 1
count = 0
for i in range(m):
    if l[i] == n:
        count += 1
print(count)