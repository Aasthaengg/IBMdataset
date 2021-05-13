from itertools import permutations
import math


x = [int(input()) for i in range(5)]

lis = list(permutations(x,5))


minimum = 0
for i in x:
    minimum += math.ceil(i/10)*10

total = 0
for l in lis:
    total = l[0]
    for i in range(1,5):
        total += math.ceil(l[i]/10)*10
    minimum = min(minimum,total)

print(minimum)