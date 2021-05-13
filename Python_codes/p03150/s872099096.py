s = input()
key = 'keyence'
n = len(s)

for i in range(n):
    for j in range(i,n):
        cmp_s = s[:i]+s[j:]
        if cmp_s == key:
            print('YES')
            exit()
print('NO')
