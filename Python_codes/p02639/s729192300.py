Xlist=list(map(int,input().split()))

ans=1
for X in Xlist:
	if X==0:
		print(ans)
	else:
		ans=ans + 1