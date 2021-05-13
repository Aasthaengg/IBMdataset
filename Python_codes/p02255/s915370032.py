import sys

def printlist(lst):
	for l in lst:
		print(l),
	print

N = int(sys.stdin.readline().strip())
A = sys.stdin.readline().strip().split(" ")

A = map(lambda x:int(x),A)
for i in range(0,N):
	temp = A[i]
	j = i-1
	while j>=0 and A[j]>temp:
		A[j+1] = A[j]
		j-=1
	A[j+1]=temp
	printlist(A)