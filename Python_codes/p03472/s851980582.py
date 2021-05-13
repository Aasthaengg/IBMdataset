import math
n,h = map(int ,raw_input().split())
ais = [map(int, raw_input().split()) for _ in range(n)]
ais.sort(key = lambda x: (-x[1],x[0]))
cumul = 0
r = +float('inf')
m = max(ais)[0]
for i in range(-1,len(ais)):
	if i >= 0:
		cumul += ais[i][1]

	if cumul >= h:
		r = min(r, (i+1))
		break
	else:
		r = min(r, i+1 + math.ceil(abs(h - cumul) /  float(m)))
print int(r)