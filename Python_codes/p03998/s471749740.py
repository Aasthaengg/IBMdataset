
import collections
h = {p: collections.deque(list(raw_input())) for p in 'abc'}	
t = 'a'
while(True):
	if len(h[t]) == 0:
		print t.upper()
		break
	t  = h[t].popleft()