s, t = raw_input(), raw_input()
def f(a,b):
	if len(a) != len(b): return False

	for u,v in zip(a,b):
		if u != v and u != '?':
			return False
	return True
cand = -1
for i in range(len(s)):
	if f(s[i:i + len(t)],t):
		cand = i

if cand == -1:
	print 'UNRESTORABLE'
else:
	print s[:cand].replace('?', 'a') + t + s[cand+len(t):].replace('?','a')
