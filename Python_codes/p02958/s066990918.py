import itertools
n = int(input())
p = list(map(int,input().split()))

memo = 0
mode = 1
for k in range(n):
	if memo > p[k]:
		mode = 0
		break
	memo = p[k]
if mode:
	print("YES")
	exit()

for i,j in itertools.combinations(range(n), 2):
	memo = 0
	mode = 1
	for k in range(n):
		if k == i:
			k = j
		elif k == j:
			k = i
		if memo > p[k]:
			mode = 0
			break
		memo = p[k]
	if mode:
		print("YES")
		exit()
print("NO")