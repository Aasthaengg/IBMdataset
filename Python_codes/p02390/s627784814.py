t=int(raw_input())
def sec(t):
	s= t%60
	return s
def mi(t):
	m= t//60
	while m>=60:
		m=m-60
	return m
def hr(t):
	h= t//3600
	return h
print "%d:%d:%d" % (hr(t),mi(t),sec(t))