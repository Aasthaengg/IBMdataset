n, h, w = input().split()
n = int(n)
h = int(h)
w = int(w)
a = []
b = []

for i in range(n):
	add = input().split()
	a.append(int(add[0]))
	b.append(int(add[1]))

count = 0
for i in range(n):
	if a[i] >= h and b[i] >= w:
		count += 1
	else:
		pass

print(count)