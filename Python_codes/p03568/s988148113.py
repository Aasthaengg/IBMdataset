import math
import copy

n = int(input())
a = [int(x) for x in input().split()]
neko = 3 ** n
nya = 1
for i in a:
    if i%2 == 0:
        nya *= 2
print(neko-nya)