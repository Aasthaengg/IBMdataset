import itertools

H, W = map(int, input().split())
S = [input() for _ in range(H)]

SS = [[0 for _ in range(W)] for _ in range(H)]

for h in range(H):
	for w in range(W):
		if '#' in S[h][w] : SS[h][w] = -1

for h in range(H):
	for w in range(W):
		if SS[h][w] == -1:
			for y, x in itertools.product([-1, 0, 1], [-1, 0, 1]):
				if 0 <= h+y < H and 0 <= w+x < W:
					if SS[h+y][w+x] != -1 :
						SS[h+y][w+x] += 1

for h in range(H):
	for w in range(W):
		if SS[h][w] == -1:print('#', end="")
		else : print(SS[h][w], end="")
	print()