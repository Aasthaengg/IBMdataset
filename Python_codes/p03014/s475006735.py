H, W = map(int, input().split())
grid = [input() for i in range(H)]

tate = [[0] * W for i in range(H)]
yoko = [[0] * W for i in range(H)]

for i in range(H):
	for j in range(W):
		if grid[i][j] == ".":
			if tate[i][j] == 0:
				back = 0
				while(1):
					if 0 > i - back or grid[i - back][j] == "#":
						break
					else:
						back += 1
				forth = 0
				while(1):
					if i + forth >= H or grid[i + forth][j] == "#":
						break
					else:
						forth += 1
				for k in range(-back + 1, forth):
					tate[i + k][j] = forth + back - 1
			if yoko[i][j] == 0:
				back = 0
				while(1):
					if 0 > j - back or grid[i][j - back] == "#":
						break
					else:
						back += 1
				forth = 0
				while(1):
					if j + forth >= W or grid[i][j + forth] == "#":
						break
					else:
						forth += 1
				for k in range(-back + 1, forth):
					yoko[i][j + k] = forth + back - 1

maxl = 0
for i in range(H):
	for j in range(W):
		maxl = max(maxl, tate[i][j] + yoko[i][j] - 1)
print(maxl)