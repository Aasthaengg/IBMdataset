a, b = map(int, input().split())
cnt = 0
for i in range(a, b + 1):
    flag = True
    si = str(i)
    for j in range(len(si) // 2):
        if si[j] != si[-(j + 1)]:
            flag = False
    if flag:
        cnt += 1
print(cnt)