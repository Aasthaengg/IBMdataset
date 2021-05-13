#!/home/matsumotokazuho/.pyenv/shims/pypy
# import math
# from copy import deepcopy
# from operator import itemgetter
# from collections import defaultdict
# from collections import Counter
from collections import deque
# import itertools
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

H, W, = map(int, input().split())
Map = [input().rstrip() for _ in range(H)]
# print(Map)

White = 0
White += Map[0].count('.', 1)
for i in range(1, H - 1):
    White += Map[i].count('.')
White += Map[-1].count('.', 0, -1)

s = (0, 0)
e = (H-1, W-1)

dis = [[-1]*W for _ in range(H)]

q = deque()
q.append(s)
dis[q[0][0]][q[0][1]] = 0
while q:
    for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        y, x = [o + d for o, d in zip(q[0], delta)]
        if y < 0 or H - 1 < y or x < 0 or W - 1 < x:
            pass
        elif Map[y][x] == '#':
            pass
        elif dis[y][x] != -1:
            pass
        else:
            dis[y][x] = dis[q[0][0]][q[0][1]] + 1
            q.append((y, x))
            if (y, x) == e:
                break
    else:
        q.popleft()
        continue
    break

if dis[e[0]][e[1]] == -1:
    print(-1)
else:
    print(White-(dis[e[0]][e[1]]-1))
