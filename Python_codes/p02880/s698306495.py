num = int(input())

for i in range(1, 10):
	for j in range(1, 10):
		if (i * j) / num == 1:
			print("Yes")
			exit()

print("No")