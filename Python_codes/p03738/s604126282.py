def f(a, b):
	if len(a) != len(b):
		return 'GREATER' if len(a) > len(b) else 'LESS'
	for u,v in zip(a,b):
		if int(u) < int(v):
			return 'LESS'
		elif int(u) > int(v):
			return 'GREATER'
	return  'EQUAL'

print f(raw_input(), raw_input())