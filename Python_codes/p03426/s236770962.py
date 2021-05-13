H, W, D = map(int, input().split())
a = [[0, 0] for i in range(H * W)]
for i in range(H):
	A = [int(j) for j in input().split()]
	for j in range(W):
		a[A[j] - 1][0] = i
		a[A[j] - 1][1] = j
Q = int(input())
b = [0] * H * W
i = D
while i < H * W:
	b[i] += abs(a[i - D][0] - a[i][0])
	b[i] += abs(a[i - D][1] - a[i][1])
	b[i] += b[i - D]
	i += 1
for i in range(Q):
	L, R = map(int, input().split())
	print(b[R - 1] - b[L - 1])