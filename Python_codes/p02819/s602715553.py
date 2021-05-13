# -*- coding:utf-8 -*-
X = int(input())

sosu_list = [2]

for num in range(3,X+1,2):
    if all(num%sosu != 0 for sosu in sosu_list):
        sosu_list.append(num)

if X == sosu_list[-1]:
    print(X)
else:
    if X % 2 ==0:
        X+=1
    while True:
        if all(X%sosu != 0 for sosu in sosu_list):
            print(X)
            break
        X += 2
