dim = [0,0,0,0]

for _ in range(3):
	a, b = [int(x) for x in input().split()]
	dim[a-1] += 1
	dim[b-1] += 1

if 3 in dim:
	print("NO")
else:
	print("YES")