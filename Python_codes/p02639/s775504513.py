a = [int(x) for x in input().split(" ")]
for i, x in enumerate(a):
	if x == 0:
		print(i+1)  