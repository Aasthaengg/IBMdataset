n = int(input().rstrip())
a = [int(i) for i in input().rstrip().split()]
v = 0.0
for i in range(len(a)):
	v = v + 1 / a[i]

print(1 / v)
