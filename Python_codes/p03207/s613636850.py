# coding: utf-8

num = int(input())
table = []
total = 0
for i in range(num):
    table.append(int(input()))
list.sort(table)
total += table[num-1] / 2
for i in range(num-1):
    total += table[i]
print(int(total))