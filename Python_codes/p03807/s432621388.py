N=int(input())
L=list(map(int,input().split()))
C=0
for i in range(N):
	if L[i]%2==1:
		C+=1
if C%2==1:
	print("NO")
else:
	print("YES")