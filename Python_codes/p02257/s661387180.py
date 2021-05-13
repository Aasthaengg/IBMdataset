# coding: UTF-8
n = int(raw_input())
count = 0
for i in range(n):
    num = int(raw_input())
    if (num < 2):
        continue
    elif (num == 2):
        count += 1
        continue
    elif (num % 2 == 0):
        continue
    if pow(2,num-1,num) == 1:
        count += 1
print(count)

