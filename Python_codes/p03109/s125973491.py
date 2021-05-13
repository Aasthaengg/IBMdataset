s = raw_input()
y,m,d = map(int, s.split('/'))

def f(y,m,d):
	if m < 4: return True
	if m == 4 and d <= 30: return True
	return False
print 'Heisei' if f(y,m,d) else 'TBD'