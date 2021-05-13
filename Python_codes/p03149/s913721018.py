N = list(map(int, input().split()))
for i in (1, 9, 7, 4):
    if i not in N:
        print('NO')
        exit()
else:
    print('YES')
