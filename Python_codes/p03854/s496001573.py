s = input()
s = s[::-1]
j = 0
p = len(s)
while True:
    if s[j:j+5] == 'maerd':
        j += 5
    elif s[j:j+7] == 'remaerd':
        j += 7
    elif s[j:j+5] == 'esare':
        j += 5
    elif s[j:j+6] == 'resare':
        j += 6
    else:
        print('NO')
        break
    if j == p:
        print('YES')
        break