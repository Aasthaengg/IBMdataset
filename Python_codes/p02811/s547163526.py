coin = input().split(" ")
K = int(coin[0])
X = int(coin[1])
if 500 * K >= X:
	print("Yes")
else:
	print("No")