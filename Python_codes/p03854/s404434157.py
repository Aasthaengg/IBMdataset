a = ['dream','dreamer','erase','eraser']

a = [x[::-1] for x in a]

s = input()

s = s[::-1]
n = len(s)
i = 0
while i < n:
    if s[i] == 'm':
        if s[i:i+5] == 'maerd':
            i += 5
        else:
            print('NO')
            exit()
    elif s[i] == 'e':
        if s[i:i+5] == 'esare':
            i += 5
        else:
            print('NO')
            exit()
    elif s[i] == 'r':
        if s[i+2] == 'm':
            if s[i:i+7] == 'remaerd':
                i += 7
            else:
                print('NO')
                exit()
        elif s[i+2] == 's':
            if s[i:i+6] == "resare":
                i += 6
            else:
                print('NO')
                exit()
        else:
            print('NO')
            exit()
    else:
        print('NO')
        exit()
print('YES')