while True:
    h,w = map(int,raw_input().split())
    if h == 0 and w == 0:
        break
    for i in range(h):
        if i % 2 == 0:
            a = '#.'
        else :
            a = '.#'
        if w % 2 == 0:
            print a*(w/2)
        else:
            print a*(w/2)+a[0]
    print ''