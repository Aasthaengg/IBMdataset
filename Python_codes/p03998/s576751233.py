Sa = list(input())
Sb = list(input())
Sc = list(input())

card = Sa.pop()
while 1:
    if card == 'a':
        if len(Sa) > 0:
            card = Sa.pop(0)
        else:
            print('A')
            break
    elif card == 'b':
        if len(Sb) > 0:
            card = Sb.pop(0)
        else:
            print('B')
            break
    else:
        if len(Sc) > 0:
            card = Sc.pop(0)
        else:
            print('C')
            break
