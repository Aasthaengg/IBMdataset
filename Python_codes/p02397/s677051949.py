#coding: UTF-8

while 1:
    i = map(int,raw_input().split())

    i.sort()
    x = i[0]
    y = i[1]

    if x == 0 and y == 0:
        break
    else:
        print '%d %d' %(x, y)