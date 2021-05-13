sa = list(input())[::-1]
sb = list(input())[::-1]
sc = list(input())[::-1]

# A からスタート
p = sa.pop()
while len(sa) > -1 and len(sb) > -1 and len(sc) > -1:
    if p == 'a':
        if len(sa) == 0:
            print('A')
            exit()
        p = sa.pop()
    elif p == 'b':
        if len(sb) == 0:
            print('B')
            exit()
        p = sb.pop()
    elif p == 'c':
        if len(sc) == 0:
            print('C')
            exit()
        p = sc.pop()