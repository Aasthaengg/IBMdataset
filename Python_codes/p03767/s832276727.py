N=int(input())
L=list(map(int,input().split()))
L=sorted(L)
K=0
for i in range(N):
	K+=L[i*2+N]
print(K)
