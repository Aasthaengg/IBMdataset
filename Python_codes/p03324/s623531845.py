d, n = map(int, input().split())

cnt = 0
if d == 1:
    for i in range(1, 100**3 + 1):
        if i % 100 ** 1 == 0 and i % 100 ** 2 != 0:
            cnt += 1
        if cnt == n:
            print(i)
            exit()
elif d == 2:
    for i in range(1, 100 ** 4):
        if i % 100 ** 2 == 0 and i % 100 ** 3 != 0:
            cnt += 1
        if cnt == n:
            print(i)
            exit()
else:
    for i in range(1, 100**3+1):
        if i % 100 != 0:
            cnt += 1
        if cnt == n:
            print(i)
            exit()