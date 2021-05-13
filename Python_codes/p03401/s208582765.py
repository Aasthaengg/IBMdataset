# solution

import io
import sys

data = int(input())
array = [0] + [int(x) for x in input().split()] + [0]

cnt = sum(abs(array[i+1] - array[i]) for i in range(data+1))

for j in range(1, data+1):
    print(cnt - (abs(array[j]-array[j-1]) + abs(array[j+1]-array[j])) + abs(array[j+1]-array[j-1]))
