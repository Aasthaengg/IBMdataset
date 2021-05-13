n,m = map(int, raw_input().split())
r = 0
cakes = [map(int, raw_input().split()) for _ in range(n)]

for b in range(8):
	cakes.sort(key = lambda x: sum([x[i] * (-1 if ((b >> i) & 1) else 1) for i in range(3) ]))
	
	s = 0
	for i in range(n-1, n - 1 - m, -1):
		s += sum([cakes[i][j] * (-1 if ((b >> j) & 1) else +1) for j in range(3)])
	r = max(r, s)
print r