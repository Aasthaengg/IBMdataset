import math

n = int(raw_input())
num = list()
count = 0
max = 0

for i in range(n):
    num.append(int(raw_input()))

for i in range(n):
    root_num = math.sqrt(num[i])
    for j in range(2, int(root_num) + 1):
        if num[i] % j == 0:
            count = count + 1
            break

print n - count