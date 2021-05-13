A, B = map(int, input().split())
ans = 0

for i in range(A, B + 1):
    i = str(i)

    flag = True
    for j in range(len(i) // 2):
        if i[j] != i[len(i) - 1 - j]:
            flag = False
    if flag == True:
        ans += 1
print(ans)
