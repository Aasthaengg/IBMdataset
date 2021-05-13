A, B = map(int, input().split())

cnt = 0
for i in range(A, B + 1):
    num = str(i)
    if num[0] == num[-1]:
        if num[1] == num[-2]:
            cnt += 1
print(cnt)