import sys
N=int(sys.stdin.readline())
frequency=[1]*(N+1)
total=1
for i in range(2,N+1):
	for j in range(i,N+1,i):
		frequency[j]+=1
	total+=i*(frequency[i])
print(total)