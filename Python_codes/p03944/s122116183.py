def main():
	W, H, N = map(int, input().split())
	lst = [[True for _ in range(H)] for _ in range(W)]

	for _ in range(N):
		x, y, a = map(int, input().split())

		if a == 1:
			for i in range(x):
				for j in range(H):
					lst[i][j] = False
		elif a == 2:
			for i in range(x, W):
				for j in range(H):
					lst[i][j] = False
		elif a == 3:
			for i in range(W):
				for j in range(y):
					lst[i][j] = False
		elif a == 4:
			for i in range(W):
				for j in range(y, H):
					lst[i][j] = False
		
	cnt = 0

	for i in range(W):
		for j in range(H):
			if lst[i][j]:
				cnt += 1

	print(cnt)

  
if __name__ == "__main__":
  	main()