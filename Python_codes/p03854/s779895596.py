s = str(input())
r = ''.join(list(reversed(s)))
flag = [0,0,0,0]
t = ['maerd', 'remaerd', 'esare', 'resare']
while len(r) >= 0:
    if r[0:5] == t[0]:
        r = r[5:]
        flag[0] +=1
    elif r[0:7] == t[1]:
        r = r[7:]
        flag[1] +=1
    elif r[0:5] == t[2]:
        r = r[5:]
        flag[2] +=1
    elif r[0:6] == t[3]:
        r = r[6:]
        flag[3] +=1
    elif len(r) == 0:
        print('YES')
        break
    else:
        print('NO')
        break
# print(flag)