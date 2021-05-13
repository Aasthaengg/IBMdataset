#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

a,b=input2()
count=1
if b<=1:
	print(0)
else:
	for i in range(1,21):
		count=count-1+a
		if count>=b:
			print(i)
			break