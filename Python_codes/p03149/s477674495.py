pool = list(map(int, input().split()))
flag = True
for i in [1, 7, 9, 4]:
    if i not in pool:
        flag = False
print('YES' if flag else 'NO')
