elems = map(int,list(raw_input()))
k = int(raw_input())

for v in elems:
	if v == 1: 
		k -=1
	else: k = 0
	if k <= 0:
		print v
		break
