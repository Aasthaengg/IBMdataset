# coding: utf-8

list = input().rstrip().split(" ")
len = int(list[1]) - int(list[0])

count = 0

for i in range(len+1):
    num = int(list[0]) + i
    result = int(list[2]) % int(num)
    if int(result) == 0:
        count += 1

print(count)