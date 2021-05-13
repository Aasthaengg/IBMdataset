n = int(input())
m = -1
for i in range(1, n+1):
    if i * (i - 1) < 2 * n <= i * (i + 1):
        m = i
        break
top = m * (m + 1) // 2
for i in range(0, m):
    if top - i == n:
        ng = i
        break
for i in range(1, m+1):
    if i == ng:
        continue
    print(i)