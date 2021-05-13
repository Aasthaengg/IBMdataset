#coding:utf-8
#1_5_A 2015.4.1
while True:
    length,width = map(int,input().split())
    if (length,width) == (0,0):
        break
    for i in range(length):
        print('#' * width)
    print()