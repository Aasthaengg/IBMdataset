A,B,K=[int(x) for x in input().split(' ')]

lis=[]
blis=[]
count=0

sm=min([A,B])
bm=max([A,B])
for i in range(1,sm+1):
	if sm/i == sm//i:
		lis.append(i)

for i in lis:
	if bm/i == bm//i:
		blis.append(i)

blis=list(set(blis))
blis.sort()
blis.reverse()

print(blis[K-1])


#8 12 2

