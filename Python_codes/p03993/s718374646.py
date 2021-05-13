N=int(input())
L=list(map(int,input().split()))
count=0
for i in range(N):
	x=L[i]
#	print(L[i],L[L[i]-1])
	if L[x-1]==i+1:
		count+=1
print(count//2)