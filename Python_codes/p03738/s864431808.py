a = input()
b = input()

al = len(a)
bl = len(b)

if al>bl:
    print('GREATER')
elif al<bl:
    print('LESS')
else:
    i = 0
    check = 0
    for i in range(al):
        if a[i] == b[i]:
            pass
        else:
            check += int(a[i]) - int(b[i])
            break

    if check > 0:
        print('GREATER')
    elif check < 0:
        print('LESS')
    else:
        print('EQUAL')
