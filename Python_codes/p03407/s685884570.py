def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

A,B,C = inpl()

if A+B >= C:
	print('Yes')
else:
	print('No')