from collections import defaultdict

n=int(input())
A=list(map(int,input().split()))
MOD=10**9+7
L=defaultdict(int)

def soinsu(n):
	l=defaultdict(int)
	for j in range(2,int(n**0.5)+1):
		while n%j==0:
			l[j]+=1
			n//=j
	if l=={}:
			l[n]+=1
	else:
		if n!=1:
			l[n]+=1
	for k,v in l.items():
		L[k]=max(L[k],v)

for i in range(n):
	soinsu(A[i])

LM=1
for k,v in L.items():
	LM*=k**v
	LM%=MOD

r=0
for i in range(n):
	r+=LM*pow(A[i],MOD-2,MOD)
	r%=MOD
print(r)