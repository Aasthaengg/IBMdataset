import copy
import sys
N = int(input())
H = list(map(int,input().split()))
C = 0

if sorted(H) == H:
	print("YES")
	sys.exit()

for i in range(0,N-1):
	for j in range(1,N):
		L = copy.copy(H)
		L[i],L[j] = L[j],L[i] 
		if L == sorted(H):
			print("YES")
			sys.exit()
print("NO")