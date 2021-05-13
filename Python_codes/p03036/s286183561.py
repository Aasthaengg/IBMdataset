#入力:N,M(int:整数)
def input2():
	return map(int,input().split())
  
r,D,x=input2()

ans=x
for i in range(1,11):
	ans=ans*r -D
	print(ans)