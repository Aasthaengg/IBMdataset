n = int(input())
m = 0
i = 1
while True:
    m += i
    if m >= n:
        break
    i += 1
for j in range(1, i + 1):
    if not j == m - n:
        print(j)