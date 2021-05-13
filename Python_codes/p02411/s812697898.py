#-*-coding:utf-8-*-
while True:
    m,f,r = map(int,input().split())
    if m == -1 and f == -1 and r == -1:
        break
    if m == -1 or f == -1:
        print('F')
        m = -999
    if m + f >= 80:
        print('A')
    if 80 > m + f and m + f >= 65:
        print('B')
    if 65 > m + f and m + f >= 50:
        print('C')
    if 50 > m + f and m + f >= 30:
        if r >= 50:
            print('C')
        else:
            print('D')
    if 30 > m + f >= 0:
        print('F')