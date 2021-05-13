import sys

w = sys.stdin.readline().rstrip().lower()
cnt = 0
while True:
	lines = sys.stdin.readline().rstrip()
	if not lines:
		break
	for s in lines.split( " " ):
		if w == s.lower():
			cnt = cnt + 1	

print( cnt )