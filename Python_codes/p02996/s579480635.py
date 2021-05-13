n = int(input())

arr = []

for i in range(n):
	a,b = map(int,input().split())
	arr.append([b,a])

arr.sort()

now = 0

for a in arr:
	if now + a[1] > a[0]:
		print("No")
		exit()
	now += a[1]

print("Yes")
