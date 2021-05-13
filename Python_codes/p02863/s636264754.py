n,T = map(int, raw_input().split(' '))
dishes = [map(int, raw_input().split(' ')) for _ in range(n)]

#print n,T
#print dishes
h = [0 for iii in range(T + 1)]
dishes.sort(key = lambda x:x[0])
m = dishes[0][1] if len(dishes) == 1 else 0
for u,v in dishes:
	m = max(m , h[T-1] + v)
	for tt in range(T - 1, -1, -1):
		if tt - u >= 0:
			h[tt] = max(h[tt], v + h[tt - u])
		
print m
