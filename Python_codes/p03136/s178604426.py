# coding: utf-8

num = int(input())
total = 0
number = input().split(" ")
table = list(number)
x = [int(i) for i in table]
list.sort(x, reverse=True)
max = x[0]
for i in range(1, num):
    total += x[i]

if max < total:
    print("Yes")
else:
    print("No")