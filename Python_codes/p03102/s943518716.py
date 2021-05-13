n,m,q = map(int, raw_input().split(' ')) #2 3 -10
bis = map(int, raw_input().split(' '))
c = 0
for _ in range(n):
	if sum([u*v for u,v in zip(map(int,raw_input().split(' ')),bis)]) + q > 0:
		c+=1
print c
