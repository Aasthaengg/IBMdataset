H = int(input())
W = int(input())
N = int(input())



if N // H > N // W:
	print((N // W) + 1 ) if N % W != 0 else print(N // W)
else:
	print((N // H) + 1 ) if N % H != 0 else print(N // H)