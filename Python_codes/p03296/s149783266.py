n = int(input())
a = [int(i) for i in input().split()]

c = 0

for i in range(1,n):
	if a[i] == a[i-1]:
		a[i] = 10001
		c += 1

print(c)		