import numpy as np
import sys

H, W = map(int, input().split())
I = np.array(sys.stdin.read().split(), np.int64).reshape(H,-1)
grid = np.zeros([H,W])
grid[np.where(I%2==1)] = 1

h_move = np.zeros([H,W-1])
s = np.zeros(H)
for i in range(H):
	cond = 0
	for j in range(W):
		if cond == 0:
			if grid[i,j] == 0:
				continue
			else:
				if j == W-1:
					s[i] = 1
				else:
					h_move[i,j] = 1
					cond = 1
		else:
			if grid[i,j] == 0:
				if j == W-1:
					s[i] = 1
				else:
					h_move[i,j] = 1
			else:
				cond = 0
	
v_move = np.zeros(H)
cond = 0
for i in range(H-1):
	if cond == 0:
		if s[i] == 0:
			continue
		else:
			v_move[i] = 1
			cond = 1
	else:
		if s[i] == 0:
			v_move[i] = 1
		else:
			cond = 0

n = h_move.sum() + v_move.sum()

print(int(n))
for i in range(H):
	for j in range(W-1):
		if h_move[i,j] == 1:
			print(i+1,j+1,i+1,j+2)
for i in range(H-1):
	if v_move[i] == 1:
		print(i+1,W,i+2,W)
