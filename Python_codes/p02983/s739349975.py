L, R = map(int,input().split())
if R-L+1 >= 2019:
	print(0)
else:
	print(min([(i*j)%2019 for i in range(L,R+1) for j in range(i+1,R+1)]))