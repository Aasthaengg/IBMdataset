H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

ans_lst = [[0 for _ in range(W)] for _ in range(H)]

# 色ヌル場所のポインタ
pointer = [0, 0]
direction = 1

for i in range(1, N + 1):
	color_stock = A[i - 1]
	while color_stock:
		ans_lst[pointer[0]][pointer[1]] = i
		color_stock -= 1
		
		# ポインタの更新
		if pointer[1] == 0 and direction == -1:
			pointer[0] += 1
			direction = 1
		elif pointer[1] == W - 1 and direction == 1:
			pointer[0] += 1
			direction = -1
		elif direction == 1:
			pointer[1] += 1
		elif direction == -1:
			pointer[1] -= 1
		else:
			print("what!?")
			
for i in range(H):
	print(*ans_lst[i])