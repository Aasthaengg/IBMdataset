X,A,B = map(int,input().split())

if A >= B:
	print("delicious")
elif A < B and B-A <= X:
	print("safe")
elif A < B and  B-A > X:
	print("dangerous")