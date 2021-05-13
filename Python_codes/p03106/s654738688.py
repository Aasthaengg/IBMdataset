def f(a):
	r = []
	for d in range(1,int(a ** 0.5) + 1):
		if a % d == 0:
			r.append(d)	
			if d * d != a: r.append(a/d)
	return r if r else [1]
a,b,k = map(int, raw_input().split(' '))
r = []
for d in f(a):
	if d in f(b):
		r.append(d)

r.sort()

print r[-k]