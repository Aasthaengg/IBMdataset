n = list(input())

for i in range(len(n)):
    for j in range(i,len(n)):
        tmp = n[:]
        del tmp[i:j]
        if ''.join(tmp) == 'keyence':
            print('YES')
            exit()
else:
    print('NO')
