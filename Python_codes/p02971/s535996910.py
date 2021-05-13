n = int(input())
first = 0
second = 0
a = []

for i in range(n):	
	a.append(int(input()))
	if first < a[i]:
		first = a[i]
	elif second < a[i]:
		second = a[i]


for i in a:
	print(second) if i == first else print(first) 