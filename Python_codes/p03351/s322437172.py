a,b,c,d = map(int,input().split())
if max(a,c)-min(a,c) <= d:
	print("Yes")
elif max(a,b)-min(a,b) <= d and max(b,c)-min(b,c) <= d:
	print("Yes")
else:
	print("No")