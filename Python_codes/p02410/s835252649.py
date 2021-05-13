import sys
n,m=map(int,input().split())
A=[0]*n
B=[0]*m
C=[0]*n
for i in range(0,n):
	A[i]=list(map(int, input().split()))
	
for i in range(0,m):
	B[i]=int(input())
for i in range(0,n):
	for j in range(0,m):
		C[i]+=A[i][j]*B[j]	
	print(C[i])