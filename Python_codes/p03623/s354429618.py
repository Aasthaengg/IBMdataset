a=list(map(int, input().split()))
if abs(a[0]-a[1])<abs(a[0]-a[2]):
	print('A')
else:
	print('B')