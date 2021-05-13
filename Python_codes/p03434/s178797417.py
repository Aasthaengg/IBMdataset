# coding: utf-8

num = int(input())
str = input().split()
table = [int(i) for i in str]

table2 = sorted(table, reverse = True)
a_point = 0
b_point = 0

for i in range(num):
    if i % 2 == 0:
        a_point += table2[i]
    elif i % 2 == 1:
        b_point += table2[i]
print(a_point - b_point)