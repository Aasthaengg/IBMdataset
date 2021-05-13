def main():
	t, *grid = open(0)
	h, w = map(int, t.split())
	vis = [[False] * w for _ in range(h)]
	ans = 0
	for y in range(h):
		for x in range(w):
			if vis[y][x]:
				continue
			q = [(y, x, grid[y][x])]
			d = {"#": 0, ".": 0}
			while q:
				cy, cx, cc = q.pop()
				for ny, nx in ((cy + 1, cx), (cy - 1, cx), (cy, cx + 1), (cy, cx - 1)):
					if not (0 <= ny < h and 0 <= nx < w) or vis[ny][nx] or cc == grid[ny][nx]:
						continue
					nc = grid[ny][nx]
					d[nc] += 1
					vis[ny][nx] = True
					q.append((ny, nx, nc))
			ans += d["#"] * d["."]
	print(ans)

if __name__=="__main__":
	main()