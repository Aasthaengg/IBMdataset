#入力:N,M(int:整数)
def input2():
	return map(int,input().split())
  
x,a=input2()
if x<a:
	print(0)
else:
	print(10)