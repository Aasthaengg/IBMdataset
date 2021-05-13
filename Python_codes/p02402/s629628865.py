n = int(input())
a = [int(i) for i in input().split()]
a.sort()
min = a[0]
max = a[n-1]
sum = 0
for i in range(n):
	sum += int(a[i])
print("{0} {1} {2}".format(min,max,sum))