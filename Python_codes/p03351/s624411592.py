a,b,c,d=map(int,input().split())
var=0
if abs(a-c) <=d:
	var=1
elif abs(a-b)<=d and abs(b-c)<=d:
	var=1
print('Yes' if var==1 else 'No')