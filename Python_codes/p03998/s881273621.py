sa = input()
sb = input()
sc = input()

tmp = sa[0]
sa = sa[1:]
while True:
    if tmp == 'a':
        if sa=='':
            print('A')
            break
        tmp = sa[0]
        sa = sa[1:]
    elif tmp == 'b':
        if sb=='':
            print('B')
            break
        tmp = sb[0]
        sb = sb[1:]
    elif tmp == 'c':
        if sc=='':
            print('C')
            break
        tmp = sc[0]
        sc = sc[1:]