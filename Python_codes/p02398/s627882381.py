a = map(int,raw_input().split())
i=0
while a[0] <= a[1]:
	if a[2]%a[0] == 0:
		i += 1
	a[0] += 1
		
print i