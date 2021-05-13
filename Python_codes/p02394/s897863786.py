W,H,x,y,r = list(map(int, input().split()))
if ((0 <= x-r) and (r+x <= W)) and ((0 <= y-r) and (r+y <= H)):
	print("Yes")
else:
	print("No")