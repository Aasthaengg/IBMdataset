import sys
from collections import deque, defaultdict
import copy
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


N = int(input())

group = []
n = N
if N % 2 == 1:
    group.append([N])
    n -= 1

for i in range(n//2):
    group.append([n - i, i + 1])

#print(group)

edge = []

for i in range(len(group)-1):
    for x in group[i]:
        for y in group[i+1]:
            edge.append([x, y])

if len(group) > 2:
    for x in group[len(group)-1]:
        for y in group[0]:
            edge.append([x, y])

print(len(edge))

for i in edge:
    print("{0} {1}".format(i[0], i[1]))
