S = [i for i in input()]
if len(S) == 3:
	for i in reversed(S):
		print(i, end="")
else:
	for i in S:
		print(i, end="")