from collections import Counter

def resolve():
	n = int(input())
	s = input().split()
	c = Counter(s)
	if len(c.keys()) == 3:
		print('Three')
	else:
		print('Four')
resolve()