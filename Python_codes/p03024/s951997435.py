s = list(input())
i = len(s)
o = s.count('o')

if o >= 8:
    print('YES')
else:
    i = 15 - i
    if 8 - o <= i:
        print('YES')
    else:
        print('NO')