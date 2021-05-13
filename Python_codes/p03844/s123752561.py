moji = list(map(str,input().split()))
if moji[1] == "+":
	print(int(moji[0]) + int(moji[2]))
else:
	print(int(moji[0]) - int(moji[2]))