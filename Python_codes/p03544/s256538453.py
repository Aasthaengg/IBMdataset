# coding: utf-8
N = int(input())
num2 = 2
num1 = 1
num = 1
tmp = 0
i = 2

while i <= N:
    num = num1 + num2
    tmp = num
    num2 = num1
    num1 = tmp
    i += 1
print(num)