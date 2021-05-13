X, Y = map(int, input().split())
if X % Y == 0:
	print(-1)
	exit()
for i in range((10 ** 18) // X):
	if X * i % Y != 0:
		print(X * i)
		exit()
print(-1)
