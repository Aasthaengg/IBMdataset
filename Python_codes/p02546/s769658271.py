from sys import stdin
from collections import defaultdict
input = stdin.readline
# ~ T = int(input())
T = 1
for t in range(1,T + 1):
	s = input()
	s = s[:len(s) - 1]
	if s[len(s) - 1] == 's':
		s += 'es'
	else:
		s += 's'
	print(s)
