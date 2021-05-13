import math

n = int(input())
max_num = int(-(-(math.sqrt(1 + 8*n) - 1) // 2))

s = int(max_num * (1 + max_num) / 2)

d = s - n

for i in range(max_num):
    if i+1 != d:
        print(i+1)