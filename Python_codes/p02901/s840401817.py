

def compute(subset):
	r = 0
	for i in range(len(subset)):
		r +=  (1 << (subset[i]-1))
	return r	

n,m = map(int, raw_input().split(' '))
keys= []
for _ in range(m):
	cost, nk = map(int, raw_input().split(' '))
	keys.append((cost, compute( map(int, raw_input().split(' ')) )))

h = {0:0}
for cost,mask in keys:
	for uu in range(2 ** n - 1,-1,-1):
		cm = uu & mask
		cm = uu ^ (cm) 
		h[uu] = min(h[uu] if uu in h else +float('inf'), (h[cm] if cm in h else +float('inf')) + cost )
print h[2 ** n -1] if (2 ** n -1) in h and h[(2 ** n) -1] < float('inf') else -1
