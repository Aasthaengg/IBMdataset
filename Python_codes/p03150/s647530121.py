s = input()
for i in range(len(s)):
    for j in range(len(s) - 1):
        S = s[:j] + s[j+i:]
        if S == 'keyence':
            print('YES')
            exit()
else:
    print('NO')