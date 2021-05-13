s = input()[::-1]
d = {'maerd', 'remaerd', 'esare', 'resare'}

cnt = 0
while cnt + 5 <= len(s):
    if s[cnt:cnt + 5] in d:
        cnt = cnt + 5
    elif cnt + 6 <= len(s) and s[cnt:cnt + 6] in d:
        cnt = cnt + 6
    elif cnt + 7 <= len(s) and s[cnt:cnt + 7] in d:
        cnt = cnt + 7
    else:
        print('NO')
        break
else:
    print('YES')
