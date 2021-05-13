s = list(input())
p = list(input())
#print(len(p))
import sys

for i in range(len(s)):
	t=0
	for j in range(len(p)):
		if p[j] == s[(i+j)%len(s)]:
			t = t+1
			#print(p[j], s[(i+j)%len(s)])
		else:
			t = 0
		if t == len(p):
			print('Yes')
			sys.exit()

if t < len(p):
	print('No')