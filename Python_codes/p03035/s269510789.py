#入力:N,M(int:整数)
def input2():
	return map(int,input().split())
  
a,b=input2()

if a>=13:
	print(b)
elif a>=6 and a<=12:
	print(b//2)
else:
	print(0)