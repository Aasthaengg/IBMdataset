def resolve():
	p = list(map(int, input().split()))
	m =max(p)
	s = 0
	for i in p:
		if i == m:
			continue
		s += i
	if m == s:
		print("Yes")
	else:
		print("No")
resolve()