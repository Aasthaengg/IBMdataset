# coding: utf-8
n = int(input())
taro = hanako = 0
for i in range(n):
    a, b = input().split()
    if a == b:
        taro += 1
        hanako += 1
    elif a > b:
        taro += 3
    else:
        hanako += 3
print(taro, hanako)