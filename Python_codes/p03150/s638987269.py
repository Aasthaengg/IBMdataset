s = input()
n = len(s)
flag = 0
for i in range(n):
    for j in range(i, n):
        if s[:i] + s[j:] == 'keyence':
            print('YES')
            flag = 1
            break
    if flag == 1:
        break
else:
    print('NO')