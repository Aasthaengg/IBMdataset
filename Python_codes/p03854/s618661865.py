S = input()[::-1]
ss = ['maerd', 'remaerd', 'esare', 'resare']

while True:
    for s in ss:
        if S.startswith(s):
            S = S[len(s):]
            break
    else:
        if S != '':
            print('NO')
            break

    if S == '':
        print('YES')
        break
