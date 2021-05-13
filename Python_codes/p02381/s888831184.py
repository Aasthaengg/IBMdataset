import statistics

while True:
	a=int(input())
	num=[]
	if a==0:
		break
	else:
		num=list(map(int,input().split()))
	print(statistics.pstdev(num))

