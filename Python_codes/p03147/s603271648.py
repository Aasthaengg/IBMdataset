"""
8
4 23 75 0 23 96 50 100
"""

n = int(raw_input())
ais = map(int, raw_input().split(' '))

def f(ais):
	r = [0]
	for i in range(len(ais)):
		## looking for max
		if len(r) % 2:	
			if (ais[i-1] if i-1 >= 0 else 0) <= ais[i] > (ais[i+1] if i+1 < len(ais) else 0): 
				r.append(ais[i])
		else:
		## looking for min
			if (ais[i-1] if i-1 >= 0 else 0) >= ais[i] < (ais[i+1] if i+1 < len(ais) else 1000): 
				r.append(ais[i])

	t = 0
	for i in range(0,len(r),2):
		if i + 1 < len(r):
			u,v = r[i],r[i+1]
			t += v-u
	
	return t if len(ais) > 1 else ais[0]
print f(ais)