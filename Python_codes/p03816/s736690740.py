N = int(input())
A = [int(i) for i in input().split()]
a = {}
for i in A:
	if i in a:
		a[i] += 1
	else:
		a[i] = 1
b = 0
for i in a.values():
	if i % 2 == 0:
		b += 1
if b % 2:
	print(len(a) - 1)
else:
	print(len(a))