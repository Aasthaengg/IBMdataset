# solution

import io
import sys
import math

array = list(map(len, input().split('T')))
nim, mike = map(int, input().split())

tom = [set([array[0]]), set([0])]

for i in range(1, len(array)):
    nxt = set()
    for j in tom[i % 2]:
        nxt.add(j + array[i])
        nxt.add(j - array[i])
    tom[i % 2] = nxt

if nim in tom[0] and mike in tom[1]:
    print("Yes")
else:
    print("No")