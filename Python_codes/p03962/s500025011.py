def paint():
    s = input()
    slist = s.split(' ')

    a = int(slist[0])
    b = int(slist[1])
    c = int(slist[2])
    count = 1
    if a != b:
        count += 1
    if a != c and b != c:
        count += 1

    print(count)

paint()