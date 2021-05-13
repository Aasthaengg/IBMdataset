A, B, C = map(int, input().split())
flag = False
for i in range(10000):
    if (i*B + C) % A == 0:
        flag = True
        break
if flag:
    print('YES')
else:
    print('NO')