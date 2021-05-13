n = int(input())

divcnt = {n: 0 for n in range(1, (n + 1), 2)}
for i in range(1, (n + 1), 2):
    for j in range(i, (n + 1), (i * 2)):
        divcnt[j] += 1

ans = 0
for i in divcnt:
    if divcnt[i] == 8:
        ans += 1
print(ans)
