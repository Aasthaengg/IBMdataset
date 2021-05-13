N=int(input())
L=list(map(int,input().split()))
count=0
i=0
while(1):
	if i>=N-1:
		break
	elif L[i]==L[i+1]:
		count+=1
		i+=2
	else:
		i+=1
print(count)