s = input()
d={'a':0,'b':0,'c':0,}
for i in s:
    d[i] += 1
a=d['a']
b=d['b']
c=d['c']
if abs(a-b) > 1:
    print('NO')
    exit()
if abs(a-c) > 1:
    print('NO')
    exit()
if abs(c-b) > 1:
    print('NO')
    exit()
print('YES')