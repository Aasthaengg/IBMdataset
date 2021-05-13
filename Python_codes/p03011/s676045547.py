ais = map(int, raw_input().split(' '))
s = +float('inf')
for i in range(len(ais)): s = min(ais[i] + ais[(i+1) % len(ais)], s)
print s
