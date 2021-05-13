a = input().split()
n = int(a[0])
x = int(a[1])
t = int(a[2])
total = x
time = t
while total <= n:
	if(total >= n):
		break
	total += x
	time += t
print(time)
