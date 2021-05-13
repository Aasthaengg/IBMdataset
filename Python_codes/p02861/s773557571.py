import itertools
import math
n = int(input())
pos = []
for i in range(n):
    pos.append(list(map(int, input().split())))
perm = list(itertools.permutations(range(n)))
total = 0
for i in range(len(perm)):
    for j in range(1, len(perm[i])):
        pos_from = perm[i][j - 1]
        pos_to = perm[i][j]
        total += math.sqrt((pos[pos_to][0] - pos[pos_from][0]) ** 2 + (pos[pos_to][1] - pos[pos_from][1]) ** 2)
print(total / len(perm))