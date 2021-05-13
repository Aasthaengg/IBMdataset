s = ''.join(list(reversed(input())))
t = ''

while True:
    n = len(t)
    if len(s) <= n:
        if s == t:
            print('YES')
        else:
            print('NO')
        break
    if s[n] == 'm':
        t += ''.join(list(reversed('dream')))
    elif s[n] == 'e':
        t += ''.join(list(reversed('erase')))
    elif s[n:n+3] == 'rem':
        t += ''.join(list(reversed('dreamer')))
    elif s[n:n+3] == 'res':
        t += ''.join(list(reversed('eraser')))
    else:
        print('NO')
        break