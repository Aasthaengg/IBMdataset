n=int(input())
a=list(map(int,input().split()))
a.sort()
plus=[a[n-1]]
minus=[a[0]]
for i in range(1,n-1):
	if a[i]>=0:
		plus.append(a[i])
	else:
		minus.append(a[i])
print(sum(plus)-sum(minus))
k=minus[-1]
for i in range(len(plus)-1):
	print(k,plus[i+1])
	k-=plus[i+1]
t=plus[0]
for i in range(len(minus)-1):
	print(t,minus[i])
	t-=minus[i]
print(t,k)