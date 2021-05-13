s = input().split()
stk = []
for i in s:
	if i.isdigit():
		stk.append(int(i))
	else:
		a = stk.pop()
		b = stk.pop()
		if i == '+':
			stk.append(b + a)
		elif i == '-':
			stk.append(b - a)
		else:
			stk.append(b * a)
print(stk.pop())

