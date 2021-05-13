n, m = map(int, input().split())
ablis = []
for i in range(m):
    a, b = map(int, input().split())
    ablis.append((a, b))

ablis.sort(key=lambda x: x[1])

cnt = 0
last = 0

for item in ablis:
    if item[0] >= last:
        cnt += 1
        last = item[1]

print(cnt)
