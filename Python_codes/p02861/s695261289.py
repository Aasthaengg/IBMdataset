from itertools import permutations
import math

N = int(input())
XY = []
for i in range(N):
    XY.append(list(map(int, input().split())))

l = list(permutations(XY, N))
sum = 0
for i in l:
    d = 0
    for j in range(len(i)-1):
        d += math.sqrt((i[j][0] - i[j+1][0]) ** 2 + (i[j][1] - i[j+1][1]) ** 2)
    sum += d
print(sum/len(l))
