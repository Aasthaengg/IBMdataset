data = input().split(" ")
m = 0
s = 0
for i in range(3):
	a = int(data[i])
	s += a
	if a >= m:
		m = a
print(s-m)