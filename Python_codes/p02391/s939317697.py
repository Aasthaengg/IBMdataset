# -*- coding:utf-8 -*-

string = input()
array = string.split()
a,b = int(array[0]),int(array[1])

if a < b:
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("a == b")