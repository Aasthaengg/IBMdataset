exp = input().split()

s = []
tmp = 0

for x in exp:
	if x == '+':
		tmp = int(s.pop()) + int(s.pop())
		s.append(tmp)
	elif x == '-':
		tmp = -1 * (int(s.pop()) - int(s.pop()))
		s.append(tmp)
	elif x == '*':
		tmp = int(s.pop()) * int(s.pop())
		s.append(tmp)
	else:
		s.append(int(x))

print(tmp)