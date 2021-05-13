n = int(input())
k = int(input())
x = list(map(int, input().split(' ')))
a = 0

for i in range(n):
	if abs(x[i]-k) < x[i]:
		a += abs(x[i]-k) * 2
	else:
		a += x[i] * 2
print(a)