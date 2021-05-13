s = input()

while len(s) >= 5:
    if len(s) >= 5 and s[-5:] == 'dream':
        s = s[:-5]

    elif len(s) >= 7 and s[-7:] == 'dreamer':
        s = s[:-7]

    elif len(s) >= 5 and s[-5:] == 'erase':
        s = s[:-5]

    elif len(s) >= 6 and s[-6:] == 'eraser':
        s = s[:-6]

    else:
        break

if len(s) == 0:
    print('YES')
else:
    print('NO')
