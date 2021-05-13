while 1:
    b=0
    a = [int(i) for i in input()]
    if a[0] == 0:
        break
    for i in range(len(a)):
        b += a[i]
    print(b)