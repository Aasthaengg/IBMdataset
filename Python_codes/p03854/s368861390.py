s = input()

i = len(s)
while i > 0:
    if s[i - 5:i] == 'dream':
        i -= 5
    elif s[i - 7:i] == 'dreamer':
        i -= 7
    elif s[i - 5:i] == 'erase':
        i -= 5
    elif s[i - 6:i] == 'eraser':
        i -= 6
    else:
        print('NO')
        exit()
print('YES')