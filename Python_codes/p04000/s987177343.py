from collections import Counter as C;H,W,N,*L=map(int,open(0).read().split());K=[];M=[(H-2)*(W-2)]+[0]*9
for a,b in zip(*[iter(L)]*2):
	for c in range(9):
		x=b-c//3;y=a-c%3
		if H-1>y>0<x<W-1:K+=[y*W+x]
for k,v in C(C(K).values()).items():M[0]-=v;M[k]+=v
print(*M)