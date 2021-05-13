n = raw_input()
ais = map(int, raw_input().split())
c = 0
s = sum(ais)
m = +float('inf')
for a in ais[:-1]:
	c += a
	m = min(m, abs(c - s + c))
print m