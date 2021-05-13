n = int(input())
v = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
a = 0
for i in range(n):
	if v[i] - c[i] >= 0:
		a += v[i] - c[i]
print(a)