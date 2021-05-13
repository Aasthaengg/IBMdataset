def resolve():
	s = input()
	k = int(input())
	cnt = set()
	for i in range(len(s)):
		for j in range(1, k+1):
			if j > k:
				break
			cnt.add(s[i:i+j])
	v = sorted(list(cnt))[k-1]
	print(v)
resolve()