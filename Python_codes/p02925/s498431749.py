import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
a = [[]]
for _ in range(n):
    a.append(deque([int(x) for x in input().split()]))

day = 1
next_day = []
used_player = [set() for _ in range(n**2)]

# 1日目
for i in range(1, n + 1):
    if a[a[i][0]][0] == i and (i not in used_player[day]) and (a[i][0] not in used_player[day]):
        used_player[day].add(i)
        used_player[day].add(a[i][0])
        next_day.append(a[a[i][0]].popleft())
        next_day.append(a[i].popleft())

# print(a)
# print(next_day)
from copy import deepcopy
# 2日目以降
while next_day:
    day += 1
    u = deepcopy(next_day)
    next_day = []
    # print(u)
    # print(a)
    for i in u:
        if len(a[i]) > 0 and len(a[a[i][0]]) > 0:
            if a[a[i][0]][0] == i and (i not in used_player[day]) and (a[i][0] not in used_player[day]):
                used_player[day].add(i)
                used_player[day].add(a[i][0])
                next_day.append(a[a[i][0]].popleft()) 
                next_day.append(a[i].popleft())

for i in a:
    if len(i) != 0:
        print(-1)
        sys.exit()

print(day - 1)


    






