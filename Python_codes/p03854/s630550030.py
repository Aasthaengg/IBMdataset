s = ''.join(list(reversed(input())))
words = {'remaerd', 'resare', 'maerd', 'esare'}
word = ''
j = 0
for i in range(len(s)-4):
    if j == 0:
        a = s[i:i+5]
        b = s[i:i+6]
        c = s[i:i+7]
        if a in words:
            word += a
            j = 4
        elif b in words:
            word += b
            j = 5
        elif c in words:
            word += c
            j = 6
    else:
        j -= 1
if word == s:
    print('YES')
else:
    print('NO')
