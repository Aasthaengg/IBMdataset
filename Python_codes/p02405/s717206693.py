#coding:utf-8
#1_5_C 2015.4.1
while True:
    length,width = map(int,input().split())
    if length == width == 0:
        break

    line = '#.' * (width//2 + 1)
    for i in range(length):
        if i % 2:
            print(line[1:width+1])
        else:
            print(line[0:width])
    print()