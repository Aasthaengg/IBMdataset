n = int(raw_input())
a = map(int, raw_input().split())

temp = 0
cnt = 0
for i in range(n):
	flag = 0
	min = i
	for j in range(i+1,n):
		if a[min] > a[j]:
			min = j
			flag = 1
	temp = a[i]
	a[i] = a[min]
	a[min] = temp
	cnt += flag

for i in range(n):
	if i != n-1:
		print(a[i]),
	else:
		print(a[i])

print cnt