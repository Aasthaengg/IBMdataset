import collections
n,rev,q = int(raw_input()) ,False,collections.deque()

for ai in map(int, raw_input().split()):
	if rev: q.append(ai)
	else: q.appendleft(ai)
	rev ^= True

print ' '.join(map(str, list(q)[::1 if rev else -1]))