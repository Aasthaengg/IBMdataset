s = input()

if s == 'keyence':
    print('YES')
    exit()

for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        if s[:i]+s[j:] == 'keyence':
            print('YES')
            exit()
print('NO')