S = input()
A = list(set(S))
minv = len(S) // 2
for a in A:
	maxv = 0
	v = 0
	for c in S:
		if a == c:
			v = 0
		else:
			v += 1
			maxv = max(maxv, v)
	minv = min(minv, maxv)
print(minv)