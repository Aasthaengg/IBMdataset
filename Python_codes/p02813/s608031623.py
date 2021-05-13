import itertools

N=int(input())
P=list(map(int, input().split()))
Q=list(map(int, input().split()))

L=list(itertools.permutations([i for i in range(1,N+1)]))

tempP=0
tempQ=0

for i in range(len(L)):

	if list(L[i])==P:
		tempP=i
	if list(L[i])==Q:
		tempQ=i

print(abs(tempP-tempQ))