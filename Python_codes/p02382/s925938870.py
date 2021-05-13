n = int(input())
xi = list(map(int, input().split()))
yi = list(map(int, input().split()))
for i in [1,2,3,0]:
	a = 0
	for j in range(0,n):
		if i == 0 :
			if a <= abs(yi[j]-xi[j]):
				a = abs(yi[j]-xi[j])
		else:
			a = a + abs(yi[j]-xi[j])**i
	if i == 0:
		print(a)
	else:
		print(a**(1/i))

