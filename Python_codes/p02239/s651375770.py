import sys
from collections import deque

sys.setrecursionlimit(50000)

n = int(input())

data = [[] for _ in range(n)]
answer = [-1]*n
answer[0] = 0
for i in range(n):
    line = list(map(int, input().split(" ")))
    if line[1] != 0:
        for e in line[2:]:
            data[i].append(e)


def bfs(vs, count=0):
    next_vs = []
    for v in vs:
        for n_v in data[v-1]:
            if answer[n_v-1] == -1:
                answer[n_v-1] = count+1
                next_vs.append(n_v)
    if not next_vs == []:
        bfs(next_vs, count+1)


bfs([1])

for i in range(n):
    line = str(i+1) + " " + str(answer[i])
    print(line)

