n = int(input())
a = list(map(int,input().split()))

b = [0]*n
c = 0
for i in range(n):
	if a[i] < 0:
		c += 1
		b[i] = -a[i]
	else:
		b[i] = a[i]

b.sort()
if c%2 == 1:
	b[0] = -b[0]
print(sum(b))
