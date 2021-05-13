S = input()
q = False

for i in range(1 << 4):
    s = list('aKIHaBaRa')
    for j in range(4):
        flag = (i >> j) & 1
        if flag:
            if j == 0:
                s[0] = 'A'
            elif j == 1:
                s[4] = 'A'
            elif j == 2:
                s[6] = 'A'
            else:
                s[8] = 'A'
    s = ''.join(s)
    s = s.replace('a','')
    if s == S:
        q = True

if q:
    print('YES')
else:
    print('NO')