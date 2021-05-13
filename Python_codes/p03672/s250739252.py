import sys
import math
s = list(input())
for i in range(len(s)):
	s.pop()
	n = math.ceil(len(s)/2)
	if s[:n] == s[n:]:
		print(len(s))
		sys.exit()