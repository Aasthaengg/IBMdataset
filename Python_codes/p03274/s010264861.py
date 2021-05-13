import collections

n,k = map(int, raw_input().split(' '))
xis = map(int, raw_input().split(' '))
ais = [xi for xi in xis if xi >= 0]
bis = [-xi for xi in xis if xi < 0][::-1]
m = ais[k -1] if k-1 < len(ais) else +float('inf')
m = min(m, bis[k -1] if k-1 < len(bis) else +float('inf'))

for i in range(len(ais)):
	if i + 1 == k: break
	if 0 <= k - (i+1) -1 < len(bis):

		m = min(m, 2*ais[i] + bis[k - (i+1) -1])
		m = min(m, ais[i] + 2*bis[k - (i+1) -1])
print m