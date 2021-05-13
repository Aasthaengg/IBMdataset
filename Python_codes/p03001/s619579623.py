#入力:N,M(int:整数)
def input2():
	return map(int,input().split())
  
W,H,x,y=input2()

if x==W/2 and y==H/2:
	print((W*H)/2, 1)
else:
	print((W*H)/2, 0)