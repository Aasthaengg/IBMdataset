# coding: utf-8
num = int(input())
for i in range(num):
    ls = list([int(i) for i in input().split()])
    ls.sort()
    if ls[0]**2 + ls[1]**2 == ls[2]**2:
        print("YES")
    else:
        print("NO")