import sys
A=int(sys.stdin.readline(2))
D=int(sys.stdin.readline(2))
if A>=1 and A<=12:
	if D>=1 and D<=12:
		print("AMBIGUOUS")
	else:
		print("MMYY")
elif D>=1 and D<=12:
	print("YYMM")
else:
	print("NA")