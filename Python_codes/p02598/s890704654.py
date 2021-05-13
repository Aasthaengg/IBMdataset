N,K=map(int,input().split())
A=list(map(int,input().split()))
L=0;R=10**9
while(R-L>1):
	M=L+R>>1;C=0
	for i in A:C+=(i-1)//M
	if C<=K:R=M
	else:L=M
print(R)