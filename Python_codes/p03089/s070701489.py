from sys import stdin
from itertools import groupby

n = int(stdin.readline().rstrip())
li = list(map(int,stdin.readline().rstrip().split()))
lin = []

while li:
    now = 10**10
    for i,j in enumerate(li,1):
        if i == j:
            now = i
    if now == 10**10:
        print(-1)
        exit()
    lin.append(now)
    li.pop(now-1)

for i in lin[::-1]:
    print(i)