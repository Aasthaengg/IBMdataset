s=input()

if len(s) == 2:
	print(s)
else:
	tmps=list(reversed(s))
	print("".join(tmps))