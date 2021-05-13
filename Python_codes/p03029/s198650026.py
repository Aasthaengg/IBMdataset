#入力:N,M(int:整数)
def input2():
	return map(int,input().split())
  
a,p=input2()
ans=((a*3)+p)//2
print(ans)
