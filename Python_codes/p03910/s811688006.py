n = int(input())
x = 0
i = 0
while n > x:
    i += 1
    x = (i * (i + 1)) // 2

for j in range(i, 0, -1):
    if n >= j:
        n -= j
        print(j)
    if n == 0:
        break
