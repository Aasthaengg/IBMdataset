s = [list(map(int, input().split())) for _ in range(3)]
flag = 0
cnt = 0
for i in range(1, 5):
    for j in s:
        if (j[0] == i) or (j[1] == i):
            cnt += 1
    if cnt == 3:
        flag = 1
        break
    else:
        cnt = 0
        continue

if flag == 1:
    print('NO')
else:
    print('YES')
