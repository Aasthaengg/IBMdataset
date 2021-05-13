N=int(input())

a=int(input())
b=int(input())
min_number=min(a,b)
profit=b-a


for i in range(N-2):
	c=int(input())
	if profit<c-min_number:
		profit=c-min_number	
	if min_number>c:
		min_number=c


print(profit)