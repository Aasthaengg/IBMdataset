#!/home/matsumotokazuho/.pyenv/shims/pypy
# import math
# from copy import deepcopy
# from operator import itemgetter
# from collections import defaultdict
# from collections import Counter
# from collections import deque
# import pprint
# import itertools
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

H, W = map(int, input().split())
Board = [list(input().rstrip()) for _ in range(H)]

# q = deque()
q = []
# for i, j in itertools.product(range(H), range(W)):
for i in range(H):
    for j in range(W):
        if Board[i][j] == '#':
            # Board[i][j] = 0
            q.append((i, j))

ans = 0
while q:
    qq = []
    ans += 1
    for yx in q:
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            y = yx[0] + d[0]
            x = yx[1] + d[1]
            # y, x = [i+j for i, j in zip(yx, d)]
            if y < 0 or H - 1 < y or x < 0 or W - 1 < x:
                pass
            elif Board[y][x] == '.':
                # Board[y][x] = Board[q[0][0]][q[0][1]] + 1
                Board[y][x] = '#'
                qq.append((y, x))
    q = qq

# ans = max(list(itertools.chain.from_iterable(Board)))
# ans = max(itertools.chain.from_iterable(Board))
# pprint.pprint(Board)
print(ans-1)
