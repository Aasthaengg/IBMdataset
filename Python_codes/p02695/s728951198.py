from itertools import combinations_with_replacement as comb_rplc
n,m,q=map(int,input().split())
a=[0]*q
b=[0]*q
c=[0]*q
d=[0]*q
for i in range(q):
	a[i],b[i],c[i],d[i]=map(int,input().split())
ans=0

for A in comb_rplc(range(1,m+1),n):
	sum=0
	for i in range(q):
		if A[b[i]-1]-A[a[i]-1]==c[i]:
			sum=sum+d[i]
	if sum>=ans:
		ans=sum

print(ans)