n = int(input())
a = [int(i) for i in input().split()]
q = int(input())
d = { }
s = 0
for i in a:
	if i not in d:
		d[i] = 0
	d[i] += 1
	s += i
while q:
	q -= 1
	b, c = map(int, input().split())
	if b in d:
		if c not in d:
			d[c] = 0
		s += (c - b) * d[b]
		d[c] += d[b]
		del d[b]
	print(s)

