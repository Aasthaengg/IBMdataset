N=int(input())
array=[int(x) for x in input().split()]
currentsum=0
counter=0
for i in range(N):
	currentsum+=array[i]
	if i%2==0 and currentsum<=0:
		counter+=abs(1-currentsum)
		currentsum+=(1-currentsum)
	if i%2==1 and currentsum>=0:
		counter+=abs(currentsum+1)
		currentsum-=(currentsum+1)
currentsum1=0
counter1=0
for i in range(N):
	currentsum1+=array[i]
	if i%2==1 and currentsum1<=0:
		counter1+=abs(1-currentsum1)
		currentsum1+=(1-currentsum1)
	if i%2==0 and currentsum1>=0:
		counter1+=abs(currentsum1+1)
		currentsum1-=(currentsum1+1)
		
print(min(counter,counter1))