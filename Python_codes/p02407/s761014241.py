import sys

for i in range(2):
	x = map(int, raw_input().split())
x.reverse()
for c in x[0:-1]:
	print c,
print x[-1]