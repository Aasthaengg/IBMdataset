x = raw_input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
i = a
j = 0
while i <= b :
	if c % i == 0:
		j = j + 1
	i = i + 1
print j