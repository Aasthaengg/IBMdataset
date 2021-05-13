n=int(input())
l=[int(i) for i in input().split()]
l.sort()
if sum(l[:-1])>l[n-1]:
	print("Yes")
else:
	print("No")