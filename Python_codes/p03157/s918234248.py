
from collections import deque, defaultdict
import copy
import bisect
#sys.setrecursionlimit(10 ** 9)
import math
import heapq


import sys
def input():
	return sys.stdin.readline().strip()

H, W = list(map(int, input().split()))
S = []
for i in range(H):
	S.append(list(input()))
for i in range(H):
	for j in range(W):
		if S[i][j] == '#':
			S[i][j] = 0
		else:
			S[i][j] = 1

judge = [[0]*W for i in range(H)]
dxy = [[0,1],[1,0],[-1,0],[0,-1]]

total = 0
for i in range(H):
	for j in range(W):
		if judge[i][j] == 0:
			black = 0
			white = 0
			que = deque()
			que.append([i, j])
			judge[i][j] = 1
			black += S[i][j] ^ 1
			white += S[i][j]
			#print(i, j,black, white)
			while len(que) > 0:
				loc = que.popleft()
				for n in range(4):
					loc_new = [loc[0] + dxy[n][0], loc[1] + dxy[n][1]]
					if loc_new[0] >= 0 and loc_new[0] < H and loc_new[1] >= 0 and loc_new[1] < W:
						if judge[loc_new[0]][loc_new[1]] == 0 and S[loc[0]][loc[1]] ^ S[loc_new[0]][loc_new[1]] == 1:
							judge[loc_new[0]][loc_new[1]] = 1
							black += S[loc_new[0]][loc_new[1]] ^ 1
							white += S[loc_new[0]][loc_new[1]]
							que.append(loc_new)
			total += black * white
			#print(total)

print(total)