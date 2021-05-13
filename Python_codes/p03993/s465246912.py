import math
import copy

neko = 0
n = int(input())
a = [int(x) for x in input().split()]
for i in range(n):
    if i == a[a[i]-1]-1:
        neko += 1
print(int(neko/2))