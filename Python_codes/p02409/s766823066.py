n = int(input())
list = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for i in range(n):
	a,b,c,d = [int(j) for j in input().split()]
	list[a-1][b-1][c-1] += d
for i in range(4):
	for j in range(3):
		for k in range(10):
			print(" {0}".format(list[i][j][k]),end='')
		print()
	if i != 3:
		print("####################")