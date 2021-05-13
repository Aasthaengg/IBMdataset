S = input()

if S == "SSS":
	print(0)
elif S == "RRR":
	print(3)
elif S[0] == S[1] == "R" or S[1] == S[2] == "R":
	print(2)
else:
	print(1)
