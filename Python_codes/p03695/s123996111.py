import math
import numpy as np

n = int(input())
a = list(map(int, input().split()))
check = [0] * 9
for i, val in enumerate(a):
    tar = math.floor(val / 400)
    if (tar > 8):
        tar = 8

    check[int(tar)] += 1


checkA = np.array(check[:8])
#print(checkA)
num = np.count_nonzero(checkA != 0)

less = max(num, 1)
#more = min(8, num + check[8])
more = num + check[8]
# print(check[8])

print(less, more)
'''
checkA = np.array(check[:8])
num = np.count_nonzero(checkA != 0)
if (num == 0):
    num = 1
rest = 8 - num

more = min(8, num + check[8])

print(num, more)
'''
