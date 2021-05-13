N = int(input())
A = list(map(int, input().split()))

B = [0]*(N+1)

for i in range (0, N):
	B[A[i]]+=1
    
C = 0
import math

for i in range (1, N+1):
	C+=math.comb(B[i],2)
    
for i in range (0, N):
	print(C+math.comb(B[A[i]]-1,2)-math.comb(B[A[i]],2))