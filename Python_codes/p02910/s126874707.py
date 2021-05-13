# coding: utf-8

str = input()
table = list(str)
count = 0
for i in range(len(table)):
    if i % 2 == 0:
      if table[i] == 'R' or table[i] == 'U' or table[i] == 'D':
         count += 1
    elif i % 2 == 1:
      if table[i] == 'L' or table[i] == 'U' or table[i] == 'D':
         count += 1

if count == len(str):
    print("Yes")
else:
    print("No")