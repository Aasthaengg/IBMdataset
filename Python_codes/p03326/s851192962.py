N,M = map(int,input().split())
XYZ = [tuple(map(int,input().split())) for _ in range(N)]
ans = 0
for b in range(8):
	arr = []
	for x,y,z in XYZ:
		if b&1: x *= -1
		if b&2: y *= -1
		if b&4: z *= -1
		arr.append(x+y+z)
	arr.sort(reverse=True)
	ans = max(ans, sum(arr[:M]))
print(ans)