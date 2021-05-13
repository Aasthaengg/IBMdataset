
a,b,c,d=map(int,input().split())

ans = 0

if abs(a-c) <= d:
	ans = 1

if abs(a-b) <=d and abs(b-c) <= d:
	ans = 1

if ans :
	print("Yes")
else:
	print("No")