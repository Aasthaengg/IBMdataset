n = int(input())
a = list(map(int, input().split()))
c = 0
s = 0
d = 0
j = 0
for i in range(n):
	d = 0
	while j < n and s & a[j] == 0:
		s += a[j]
		j += 1
	s -= a[i]
	c += j-i
print (c)
