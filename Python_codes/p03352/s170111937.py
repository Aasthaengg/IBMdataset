x = int(input())
min = 10000
for i in range(1,1000):
	for j in range(2,40):
		if x-i**j < min and 0 <= x-i**j:
			min = x-i**j
print(x-min)