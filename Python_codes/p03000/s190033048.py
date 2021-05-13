#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))
  
n,x=input2()
L=input_array()

D=0
flag=True
for i in range(1,n+1):
	D+=L[i-1]
	if D>x:
		print(i)
		flag=False
		break
if flag:
	print(n+1)