n=int(input())
suji=[]
for i in range (n):
	suji=suji+list(map(int,input().split()))
tlist=[]
alist=[]
for i in range(2*n):
	if i%2==0:
		tlist.append(suji[i])
	else:
		alist.append(suji[i])

for i in range(n-1):
	aaa=alist[i]//alist[i+1]
	ttt=tlist[i]//tlist[i+1]
	if alist[i]%alist[i+1]!=0:
		aaa+=1
	if tlist[i]%tlist[i+1]!=0:
		ttt+=1
	k=max(aaa,ttt)
	tlist[i+1]=tlist[i+1]*k
	alist[i+1]=alist[i+1]*k

print(int(tlist[n-1]+alist[n-1]))