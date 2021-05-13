N=int(input())
sides=[int(x) for x in input().split()]
counter=0
for i in range(N-2):
	for j in range(i+1,N-1):
		for k in range(j+1,N):
			A=sorted([sides[i],sides[j],sides[k]])
			if (A[0]+A[1]>A[2]) and A[0]!=A[1] and A[1]!=A[2] and A[0]!=A[2]:
				counter+=1
				
print(counter)