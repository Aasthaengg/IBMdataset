def candy():
    s = input()
    slist = s.split(' ')

    a = int(slist[0])
    b = int(slist[1])
    c = int(slist[2])

    if (a + b) == c or (a + c) == b or (b + c) == a:
        print('Yes')
    else:
        print('No')

candy()