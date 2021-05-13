S = input()

if S.rfind("s") == len(S) - 1:
	print(S + "es")
else:
	print(S + "s")