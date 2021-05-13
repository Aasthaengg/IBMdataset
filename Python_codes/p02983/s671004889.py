#入力:N,M(int:整数)
def input2():
	return map(int,input().split())
  
l,r=input2()


if (r-l)>=2019:
	print(0)
else:
	ans=2019
	for i in range(l,r):
		for j in range(i+1,r+1):
			ans=min(ans,(i*j)%2019)
	print(ans)
