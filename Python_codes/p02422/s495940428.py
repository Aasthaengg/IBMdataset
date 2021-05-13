A = list(input())
n = int(input())

for _ in range(n):
	command = input().split(" ")
	st = int(command[1])
	en = int(command[2]) + 1

	if command[0] == "replace":
		A[st:en] = list(command[3])
	elif command[0] == "reverse":
		B = A[st:en]
		B.reverse()
		A[st:en] = B
	else:
		moji = ""
		for i in A[st:en]:
			moji += str(i)
		print(moji)

