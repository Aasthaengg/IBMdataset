import fractions
N,K=map(int,input().split())
L=list(map(int,input().split()))
tmp=0
if N==1:
	if L[0]==K:
		print("POSSIBLE")
		exit()
	else:
		print("IMPOSSIBLE")
		exit()
for i in range(1,N):
	if i==1:
		tmp=fractions.gcd(L[0],L[1])
	else:
		tmp=fractions.gcd(tmp,L[i])
if max(L)>=K and K%tmp==0:
	print("POSSIBLE")
else:
	print("IMPOSSIBLE")