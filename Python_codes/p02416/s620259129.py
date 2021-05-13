while 1:
    a = [int(x) for x in input()]
    if len(a) and a[0] == 0:
        break
    print(sum(a))
