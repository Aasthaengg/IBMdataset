N=input()
A=map(int,raw_input().split())
num=0
flag=1
while flag:
	flag=0
	for j in reversed(range(N-1)):
		if A[j+1]<A[j]:
			A[j+1],A[j]=A[j],A[j+1]
			flag=1
			num+=1

for m in range(N-1):
	print str(A[m]),
print A[N-1]
print num