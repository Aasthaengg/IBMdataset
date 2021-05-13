import collections 
N,M=map(int,input().split())
L=[]
for i in range(M):
	X,Y=map(int,input().split())
	L.append(X)
	L.append(Y)
S=collections.Counter(L)
for i,j in S.items():
	if j%2==1:
		print("NO")
		exit()
print("YES")
