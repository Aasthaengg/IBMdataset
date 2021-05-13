a = list(map(int, input().split()))
a.sort()
if abs(a[1]-a[0]) == abs(a[2]-a[1]):
	print ("YES")
else:
	print ("NO")