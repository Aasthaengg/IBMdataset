s = list(input())
n = len(s)
for i in range(n):
    for j in range(i,n):
        t = s[:i] + s[j:]
        if ''.join(t) == 'keyence':
            print('YES')
            exit(0)
print('NO')