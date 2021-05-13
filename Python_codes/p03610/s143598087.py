# coding: utf-8

str = input()
table = list(str)

for i in range(0, len(str), 2):
  print(table[i], end ='')