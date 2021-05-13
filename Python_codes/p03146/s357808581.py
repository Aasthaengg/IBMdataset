# -*- coding: utf-8
a = int(input())
b = [a]
i = 1
while True:
    if a % 2 == 0:
        a = a//2
    else :
        a = 3*a+1
    i+=1
    if a in b:
        print(i)
        break
    b.append(a)