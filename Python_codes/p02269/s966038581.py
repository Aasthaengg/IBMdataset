n = int(input())
arr = {}
for i in range(n):
		cmd = input()
		if cmd[0] == "i":
			arr[cmd[7::]] = 0
		else:
			print("yes" if cmd[5:] in arr else "no")