n = int(input())
tot=0
for i in range(1, n+1):
	tot=tot+i
	if tot>=n:
		print(i)
		break