L, R = map(int, input().split())

minimize = 2018
P = 0

if R-L >= 2019:
	print(0)
	exit()
else:
	for i in range (L, R):
		for j in range (i+1, R+1):
			P = (i*j)%2019
			if P < minimize:
				minimize = P
print(minimize)