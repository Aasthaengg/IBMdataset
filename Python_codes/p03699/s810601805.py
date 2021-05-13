n = int(raw_input()) 
ais = [int(raw_input()) for _ in range(n)]
r = 0
cumul = 0
m = +float('inf')
for i in range(0, len(ais)):
	cumul += ais[i]
	if ais[i] % 10:
		m = min(m, ais[i])

	if cumul % 10 == 0:
		r = max(r, cumul - m)
	else:
		r = max(r, cumul)

print r