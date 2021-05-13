while 1:
	s=list(input())
	if s==["-"]:
		break
	n=int(input())
	for i in range(n):
		m=int(input())
		for j in range(m):
			s.append(s.pop(0))
	print("".join(s))