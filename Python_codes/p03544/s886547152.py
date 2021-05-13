N=int(input())
L=[0]*90
L[0]=2
L[1]=1
for i in range(2,87):
	L[i]=L[i-2]+L[i-1]
print(L[N])