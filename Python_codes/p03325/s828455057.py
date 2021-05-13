N=int(input())
L=list(map(int,input().split()))
T=0
for i in L:
	if i%2==0:
		for j in range(1,40):
			if i%2**j!=0:
				T+=j-1
				break
print(T)