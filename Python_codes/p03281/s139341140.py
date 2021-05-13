n = int(input())

cnt = 0
for i in range(1, n + 1, 2):
    div = []
    for j in range(1, i + 1):
        if i % j == 0:
            div.append(j)
    if len(div) == 8:
        cnt += 1
print(cnt)