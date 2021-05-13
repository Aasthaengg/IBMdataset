s = input()
n = len(s)

i = n
while i > 0:
    if i >= 7 and s[i-7:i] == 'dreamer':
        i -= 7
    elif i >= 5 and s[i-5:i] == 'dream':
        i -= 5
    elif i >= 6 and s[i-6:i] == 'eraser':
        i -= 6
    elif i >= 5 and s[i-5:i] == 'erase':
        i -= 5
    else:
        print('NO')
        exit()
print('YES')