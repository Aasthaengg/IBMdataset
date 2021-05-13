Sa = list(input())
Sb = list(input())
Sc = list(input())

s = Sa.pop(0)
while True:
    if s == 'a':
        if Sa ==[]:
            print('A')
            break
        s = Sa.pop(0)
    elif s == 'b':
        if Sb ==[]:
            print('B')
            break
        s = Sb.pop(0)
    else:
        if Sc ==[]:
            print('C')
            break
        s = Sc.pop(0)
