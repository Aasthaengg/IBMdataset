n, q = map(int, input().split())

p = []
time = 0

for i in range(n):
	p.append(input().split())
	p[i][1] = int(p[i][1])

while(len(p) > 0):
	if (p[0][1]<= q):
		time += p[0][1]
		print("{0} {1}".format(p[0][0], time))
		p.pop(0)
	else:
		time += q
		p[0][1] -= q
		p.append(p[0])
		p.pop(0)