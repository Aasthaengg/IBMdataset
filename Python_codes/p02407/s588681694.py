num = int(input())
data = list(map(int, input().split()))

lengh = len(data)
for tmp in range(lengh):
	if tmp == lengh-1:
		print(data.pop(-1))
	else:
		print(data.pop(-1), end=" ")
