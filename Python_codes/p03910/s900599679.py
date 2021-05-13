n = int(input())
for i in range(n):
    if (i + 1) * (i + 2) // 2 >= n:
        m = i + 1
        d = (i + 1) * (i + 2) // 2 - n
        break
for i in range(m):
    if i + 1 == d:
        continue
    else:
        print(i + 1)