i = 0
a,b,c = list(map(int, input().split()))
for d in range(a,b+1):
	e = c % d
	if (e == 0):
		i += 1
print(i)