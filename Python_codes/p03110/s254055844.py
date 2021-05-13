n = int(raw_input())
q= 0 
for _ in range(n):
	u,v = raw_input().split(' ')
	u = float(u)
	h = {'BTC':380000.0, 'JPY':1.0}
	q += u * h[v]
print q
