l = sorted([int(v) for v in input().rstrip().split()])
r = 'No'
if (l[0] == l[1] and l[0] != l[2]) or (l[1] == l[2] and l[0] != l[1]):
	r = 'Yes'

print(r)
