a = [int(i) for i in input().split()]
k = int(input())
a.sort()
note = a[2]
for i in range(k):
	note *= 2
print(a[0] + a[1] + note)
