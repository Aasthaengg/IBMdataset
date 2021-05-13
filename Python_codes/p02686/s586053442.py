n = int(raw_input())
def gb(s):
	bal = 0
	m = 0
	for l in s: 
		bal += 1 if l == '(' else -1
		m = min(m, bal)
	return (bal,m)


adds, dels = [], []
for _ in range(n):
	e = gb(raw_input())
	if e[0] >= 0:
		adds.append(e)
	else:
		dels.append(e)
adds.sort(key = lambda x: (-x[1], -x[0]))
dels.sort(key = lambda x: (x[1] - x[0], -x[0]))
def f(adds, dels):
	s = 0
	for aa,bb in adds:

		if s + aa < 0:
			return False
		if s + bb < 0:
			return False
		s += aa
		

	for aa,bb in dels:

		if s + aa < 0:
			return False
		if s + bb < 0:
			return False
		s += aa
	return s == 0

print 'Yes' if f(adds, dels) else 'No'