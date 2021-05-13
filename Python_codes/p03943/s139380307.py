l=[int(x) for x in input().split()]

a=max(l)
if (sum(l)-a)==a:
	print("Yes")
else:
	print("No")
