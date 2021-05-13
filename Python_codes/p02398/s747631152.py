x = (list(map(lambda x : int(x), input().split(" "))))
count = 0
for i in range(x[0], x[1]+1):
	if x[2] % i == 0:
		count += 1
print(count)