while True:
    x = input().split()
    a, b = int(x[0]), int(x[1])
    if a == 0 and b == 0:
        break
    if a > b:
        a, b = b, a
    print('%d %d' % (a, b))
