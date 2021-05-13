s = input()
t = ''

i = 0

while True:
    if s == t:
        print('YES')
        exit();
    elif s[i:i+7] == 'dreamer' and s[i+7:i+8] != 'a':
        t += 'dreamer' 
        i += 7
    elif s[i:i+5] == 'dream':
        t += 'dream'
        i += 5
    elif s[i:i+6] == 'eraser':
        t += 'eraser'
        i += 6
    elif s[i:i+5] == 'erase':
        t += 'erase'
        i += 5
    else:
        print('NO')
        exit()
