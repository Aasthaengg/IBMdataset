import sys
n=int(input())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

difflist=[]
for i in range(n):
	difflist.append(blist[i]-alist[i])

needcount=sum(difflist)
if needcount < 0:
	print("No")
	sys.exit()
elif needcount == 0:
	for diff in difflist:
		if diff != 0:
			print("No")
			sys.exit()
	print("Yes")
	sys.exit()

posineed=0
neganeed=0

for diff in difflist:
	if diff < 0:
		neganeed += -diff
	elif diff > 0:
		posineed += diff // 2
	if diff % 2 == 1:
		posineed += 1
		neganeed += 1

if posineed >= neganeed:
	print("Yes")
else:
	print("No")

