
A = list(input())
n = int(input())

for _ in range(n):
	command = input().split(" ")
	st = int(command[1])
	en = int(command[2]) + 1

	if command[0] == "replace":
		A[st:en] = list(command[3])
	elif command[0] == "reverse":
		A[st:en] = reversed(A[st:en])
	else:
		print(*A[st:en],sep="")

