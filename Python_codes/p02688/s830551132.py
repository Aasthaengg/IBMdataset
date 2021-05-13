N,K=map(int,input().split())
d=[]
A=[]
for i in range(K):
	d.append(input())
	arr=input().split()
	A.append(arr)
B=[]
for i in range(len(A)):
	for j in range(len(A[i])):
		B.append(int(A[i][j]))
count=0
for i in range(1,N+1):
	if i not in B:
		count+=1
print(count)