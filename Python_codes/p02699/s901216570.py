l = list(map(int,input().split(' ')))
S = l[0]
W = l[1]
if (W>=S):
	print("unsafe")
else:
	print("safe")