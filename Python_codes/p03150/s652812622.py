s = input()

flag = False
n = len(s)
for i in range(n):
    for j in range(i,n):
        if 'keyence' == s[:i] +s[j:]:
            flag = True

if flag:
    print('YES')
else:
    print('NO')