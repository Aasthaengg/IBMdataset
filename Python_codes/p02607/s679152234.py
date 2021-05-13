import math

n=int(input())
L=list(map(int,input().split()))
count=0
for i in range(0,n,2):
	if(L[i]%2==1):
		count+=1
print(count)

