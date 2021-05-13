# coding: utf-8

num = int(input())
str = input().split()
table = [int(i) for i in str]
list.sort(table)
print(table[num-1] - table[0])