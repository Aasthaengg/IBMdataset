import sys
from collections import deque

input()
d = deque()
for l in sys.stdin:
	s = l.split()
	if s[0] == 'insert':
		d.appendleft(s[1])
	elif s[0] == 'delete':
		try: d.remove(s[1])
		except: pass
	elif s[0] == 'deleteFirst':
		d.popleft()
	elif s[0] == 'deleteLast':
		d.pop()
print(*d)
