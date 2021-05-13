import sys
import math

count = 0

num_list = []

for line in sys.stdin.readlines():
    num_list.append(int(line.strip()))

num_list.remove(num_list[0])

for num in num_list:
        flag = 0
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                flag = 1
                break
        if flag == 0:
            count += 1

print count