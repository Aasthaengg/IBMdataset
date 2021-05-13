p = lambda x,y:x+y
m = lambda x,y:x-y
t = lambda x,y:x*y
ope = {'+':p, '-':m, '*':t}

data = [int(s) if s.isdigit() else s for s in input().split()]
while len(data) > 1:
	isope = [isinstance(d,str) for d in data]
	ope_idx = isope.index(True)
	xy = data[ope_idx-2:ope_idx]
	ans = ope[data[ope_idx]](*xy)
	data = data[:ope_idx-2] + [ans] + data[ope_idx+1:]

print(data[0])