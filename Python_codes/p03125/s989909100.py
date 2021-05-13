N = list(map(int,input().split()))
if(N[1]%N[0]==0):
	print(N[0]+N[1])
else:
	print(N[1]-N[0])