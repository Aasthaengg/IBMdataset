while True:
    m, f, r = [int (x) for x in input().split(' ')]
    if m == -1 and f == -1 and r == -1: break
    if m == -1 or f == -1 or m + f < 30:
        print('F')
    elif m + f >= 80:
        print('A')
    elif m + f >= 65 and m + f < 80:
        print('B')
    elif m + f >= 50 and m + f < 65:
        print('C')
    elif m + f >= 30 and m + f < 50:
        if r >= 50:
            print('C')
        else:
            print('D')