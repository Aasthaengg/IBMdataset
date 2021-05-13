N,_,*L=map(int,open(0).read().split())
A=[0]*N
for l in L: A[l-1]+=1
print(*A,sep='\n')