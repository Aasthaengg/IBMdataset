# coding:utf-8
s = input()
n = len(s)
for i in range(n):
    if s[:i] + s[n-7+i:] == 'keyence':
        print('YES')
        exit()
print('NO')
