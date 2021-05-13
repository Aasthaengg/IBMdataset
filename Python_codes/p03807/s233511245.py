n = int(input())
a = [int(_) for _ in input().split()]

cnt = 0
for i in a:
    if i % 2 != 0:
        cnt += 1
if cnt % 2 == 0:
    print('YES')
else:
    print('NO')
