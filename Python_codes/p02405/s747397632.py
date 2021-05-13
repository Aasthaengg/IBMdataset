while True:
    h, w = [int(i) for i in input().split(' ')]
    if h ==0 and w ==0:
        break
    for i in range(h):
        row = ''
        for j in range(w):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                row = row + '#'
            else:
                row = row + '.'
        print(row)
    print('')
