a = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
n = int(input())

for i in range(n):
	b, f, r, v = map(int, input().split())
	a[b-1][f-1][r-1] += v

for k in range(4):
	for j in range(3):
		for i in range(10):
			print(" {}".format(a[k][j][i]), end="")
		print("")
	if not k == 3: print("#" * 20)