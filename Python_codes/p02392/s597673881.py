a,b,c= map(int,input().split())
flg= 0
if(a<b):
	if(b<c):
		print("Yes")
		flg=1

if(flg==0):
	print("No")