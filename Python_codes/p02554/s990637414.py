num=int(input())
num2=[10, 9 ,8]

num2a=map(int, num2)

def multi(x):
	y=x**num
	return y


a, b, c=map(multi, num2a)
print((a-2*b+c)%(int(1e9+7)))