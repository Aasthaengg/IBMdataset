S = input()

dm, dr, ee, er = 'dream', 'dreamer', 'erase', 'eraser'

word = [dm[::-1], dr[::-1], ee[::-1], er[::-1], ]

s = S[::-1]

while s:
    for i in range(4):
        if s.startswith(word[i]):
            s = s[len(word[i]):]
            break
    else:
        print('NO')
        break
else:
    print('YES')
