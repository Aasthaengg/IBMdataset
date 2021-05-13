import math
t = 1
# t = input()
# t = int(t)
def max(a,b):
	if a > b:
		return a
	return b
while t > 0:
	t -= 1
	a,b = map(int,input().strip().split())
	j = 1
	ma = {}
	mb = {}
	if a%2 == 0:
		ma[2] = 1
		while a%2 == 0:
			a /= 2
	p = math.sqrt(a) + 1
	p = int(p)
	for i in range(3,p,2):
		if a%i == 0:
			ma[i] = 1
			while a%i == 0:
				a /= i
	if a > 2:
		ma[a] = 1
	if b%2 == 0:
		mb[2] = 1
		while b%2 == 0:
			b /= 2
	p = math.sqrt(b) + 1
	p = int(p)
	for i in range(3,p,2):
		if b%i == 0:
			mb[i] = 1
			while b%i == 0:
				b /= i
	if b > 2:
		mb[b] = 1
	ans = 1
	for x,y in ma.items():
		if x in mb:
			ans += 1
	print(ans)
