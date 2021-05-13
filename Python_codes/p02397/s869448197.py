while True:
    x = input().split()
    x_int = [int(i) for i in x]
    if x_int[0] == 0 and x_int[1] == 0:
        break
    else:
        x_int.sort()
        print('{} {}'.format(x_int[0],x_int[1]))