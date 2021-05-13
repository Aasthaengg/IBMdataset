n=int(input())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

plist=[]
nval=0
ncounter=0

for i in range(n):
	if alist[i] > blist[i]:
		plist.append(alist[i]-blist[i])
	elif alist[i] < blist[i]:
		nval += blist[i] - alist[i]
		ncounter += 1

plist.sort(reverse = True)
i=0
maxi=len(plist)
pcounter = 0

while nval != 0 and i < maxi:
	pcounter += 1
	nval = max(0,nval-plist[i])
	i += 1

if nval == 0:
	print(pcounter + ncounter)
else:
	print(-1)
