xi = list(map(int, input().split()))

if xi[0]*xi[1] == 0 and xi[0]*xi[2] == 0:
	print(1)
elif xi[1]*xi[2] == 0 and xi[1]*xi[3] == 0:
	print(2)
elif xi[2]*xi[3] == 0 and xi[2]*xi[4] == 0:
	print(3)
elif xi[3]*xi[4] == 0 and xi[3]*xi[0] == 0:
	print(4)
else:
	print(5)