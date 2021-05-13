# -*- coding: utf-8 -*-
from collections import deque

N,M = list(map(int, input().rstrip().split()))
AB_list = [list(map(int, input().rstrip().split())) for i in range(M)]
#-----

edge_dic = {}

# "idx 0" doesn't use
# 1: visited, 0: not visited
visited = [1] + [0]*N

# We use on and after "idx 2"
guidepost = [0]*2 + [None]*(N-1)


for a,b in AB_list:
    edge_dic.setdefault(a, [])
    edge_dic[a].append(b)
    
    edge_dic.setdefault(b, [])
    edge_dic[b].append(a)


queue = deque([1])
visited[1] = 1

while queue:
    current = queue.popleft()
    
    for next_room in edge_dic[current]:
        if visited[next_room] == 0:
            guidepost[next_room] = current
            visited[next_room] = 1
            queue.append(next_room)


if (visited.count(0) == 0) and (guidepost.count(None) == 0):
    print("Yes")
    
    for num in guidepost[2:]:
        print(num)
    
else:
    print("No")
