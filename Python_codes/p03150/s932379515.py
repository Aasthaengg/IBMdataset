s = str(input())
n = len(s)
for i in range(n):
    for j in range(i, n):
        t = s[0:i]+s[j:]
        if t == 'keyence':
            print('YES')
            exit()
else:
    print('NO')
