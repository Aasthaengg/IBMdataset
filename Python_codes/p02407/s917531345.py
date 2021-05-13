n = int(input())
a = [int(i) for i in input().split()]
a.reverse()
for i in range(n-1):
	print(a[i], end=' ')
print(a[n-1])