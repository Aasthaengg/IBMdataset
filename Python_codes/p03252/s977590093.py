s,t = raw_input(), raw_input()
def f(s,t):
	cc = {}
	cr = {}
	for u,v in zip(s,t):
		if u in cc:
			if cc[u] != v: return False
		if v in cr:
			if cr[v] != u: return False
		
		cc[u] = v
		cr[v] = u
	return True
print 'Yes' if f(s,t) else 'No'