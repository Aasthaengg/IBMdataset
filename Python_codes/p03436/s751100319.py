h,w = map(int,input().split())
s = [0]*h
white = 0
for i in range(h):
	s[i] =  input()
	s[i] = list(s[i])
	for j in range(w):
		if s[i][j] == '.':
			white += 1

def clear_maze(sx, sy, gx, gy, maze):

	INF = 100000000

	field_x_length = len(maze)
	field_y_length = len(maze[0])
	distance = [[INF for i in range(field_y_length)] for j in range(field_x_length)]
#	distance = [[INF]*field_y_length]*field_x_length

	def bfs():
		queue = []

		queue.insert(0, (sx, sy))

		distance[sx][sy] = 0

		while len(queue):
			x, y = queue.pop()

			if x == gx and y == gy:
				break

			for i in range(0, 4):
				nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]

				if (0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length and maze[nx][ny] != '#' and distance[nx][ny] == INF):
					queue.insert(0, (nx, ny))
					distance[nx][ny] = distance[x][y] + 1

		return distance[gx][gy]
	return bfs()
if clear_maze(0, 0, h-1, w-1, s) == 100000000:
	print(-1)
else:
	print(white - clear_maze(0, 0, h-1, w-1, s) - 1)