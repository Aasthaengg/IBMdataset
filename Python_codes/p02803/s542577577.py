def resolve():
	import numpy as np
	from collections import deque

	h, w = map(int, input().split())
	s = [input() for i in range(h)] # [[input()] for ...] は誤答 （文字列も配列であることを考えると3重配列になっちゃう） 
	directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] # [y軸, x軸]
	ans = 0

	for sh in range(h): # start hight
		for sw in range(w):
			if s[sh][sw] == "#":
				continue
			distance = [[-1 for j in range(w)] for i in range(h)]
			distance[sh][sw] = 0
			q = deque([[sh, sw]]) # 1段目の[]はdequeの引数がイテラブルであるため、2段目の[]はy軸x軸のペアを表現するため

			while q:
				y, x = q.popleft() # アンパックしてくれる
				for i, j in directions:
					ny, nx = y+i, x+j

					# エリア内判定
					if not ((0 <= ny < h) and (0 <= nx < w)):
						continue
					# 壁判定
					elif s[ny][nx] == "#":
						continue
					# 訪問済み判定
					elif distance[ny][nx] != -1:
						continue

					distance[ny][nx] = distance[y][x] + 1
					q.append([ny, nx]) # q.append([[ny, nx]]) は誤答
			#ans = max(ans, max(max(distance)))
			ans = max(ans, np.max(distance))
	print(ans)
resolve()