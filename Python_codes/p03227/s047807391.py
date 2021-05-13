# coding: utf-8

a = str(input())

if len(a) == 2:
    print(a)
else:
    list_a = list(a)
    for i in range(0, 3):
        print(list_a[2-i], end="")
