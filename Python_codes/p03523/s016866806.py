S = str(input())

akibalst = []
for i in range(2):
    if i == 0:
        a1 = 'A'
    else:
        a1 = ''
    for j in range(2):
        if j == 0:
            a2 = 'A'
        else:
            a2 = ''
        for k in range(2):
            if k == 0:
                a3 = 'A'
            else:
                a3 = ''
            for l in range(2):
                if l == 0:
                    a4 = 'A'
                else:
                    a4 = ''

                tmp = a1 + 'KIH' + a2 + 'B' + a3 + 'R' + a4
                akibalst.append(tmp)
#print(akibalst)
if S in akibalst:
    print('YES')
else:
    print('NO')