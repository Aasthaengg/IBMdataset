N = []
while True:
	a = list(map(int, input().split(' ')))
	if a[0] == 0 and a[1] == 0:
		break
	a.sort()
	N.append(a)
	
for i in range(len(N)):
	print(N[i][0], N[i][1])