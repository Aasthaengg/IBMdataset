
import sys
from collections import deque, defaultdict
import copy
import bisect
sys.setrecursionlimit(10 ** 9)
import math
import heapq
from itertools import product, permutations,combinations
import fractions

import sys
def input():
	return sys.stdin.readline().strip()

H, W = list(map(int, input().split()))
G = []
for i in range(H):
	G.append(input())

tansaku = [[0]*W for _ in range(H)]
total = 0
for i in range(H):
	for j in range(W):
		if tansaku[i][j] == 0 and G[i][j] == '#':
			tansaku[i][j] = 1
			black = 1
			white = 0
			que = deque([])
			que.append((i, j))
			delta = ((0, 1), (0, -1), (1, 0), (-1, 0))
			while len(que) > 0:
				loc = que.popleft()

				for d in range(4):
					x = loc[0] + delta[d][0]
					y = loc[1] + delta[d][1]
					if x >= H or y >= W or x < 0 or y < 0:
						continue

					if tansaku[x][y] == 0:
						if G[loc[0]][loc[1]] == '#' and G[x][y] == '.':
							white += 1
							tansaku[x][y] = 1
							que.append((x, y))
							#print((x, y), loc)
						elif G[loc[0]][loc[1]] == '.' and G[x][y] == '#':
							black += 1
							tansaku[x][y] = 1
							que.append((x, y))
							#print((x, y), loc, 1)
			total += black*white
			#print(i, j, black, white)
print(total)
