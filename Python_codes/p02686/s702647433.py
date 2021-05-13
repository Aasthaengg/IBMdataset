n = int(raw_input())
def gb(s):
	bal,m = 0,0
	for l in s: 
		bal += 1 if l == '(' else -1
		m = min(m, bal)
	return (bal,m)


rs = [gb(raw_input()) for _ in range(n)]
rs.sort(key = lambda x: (0,-x[1], x[0]) if x[0]>=0 else (1,x[1] - x[0], -x[0]))

def f(rs):
	s = 0
	for aa,bb in rs:
		if s + bb < 0: return False
		s += aa
	return s == 0

print 'Yes' if f(rs) else 'No'