import sys
s = int(input())
cop = []
cop.append(s)
if s%2 == 0:
	s //= 2
else:
	s = 3*s + 1

for i in range(1,1000):
	if s in cop:
		print(i+1)
		sys.exit()
	else:
		cop.append(s)
		if s%2 == 0:
			s //= 2
		else:
			s = 3*s + 1	