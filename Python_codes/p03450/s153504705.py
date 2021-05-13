# D - People on a Line

import sys
sys.setrecursionlimit(10000000)

N, M = map(int, sys.stdin.buffer.readline().split())
LRD = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(M)]

LRD = [[LRD[i][0]-1, LRD[i][1]-1, LRD[i][2]] for i in range(M)]

if N == 1 or M == 0:
    print("Yes")
    exit()

neighbor = [[] for _ in range(N)]
for i in range(M):
    neighbor[LRD[i][0]].append([LRD[i][1], LRD[i][2]])
    neighbor[LRD[i][1]].append([LRD[i][0], -LRD[i][2]])

x = [None] * N

def check(i):
    if x[i] == None:
        x[i] = 0
    for next_point, dist in neighbor[i]:
        if x[next_point] == None:
            x[next_point] = x[i] + dist
            check(next_point)
        elif x[next_point] != x[i] + dist:
            print('No')
            exit()

for i in range(N):
    if x[i] == None:
        check(i)

print('Yes')