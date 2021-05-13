stk = []
for c in input().split():
	if c in "+-*":
		a = stk.pop()
		b = stk.pop()
		stk.append(str(eval(b + c + a)))
	else:
		stk.append(c)
print(stk.pop())

