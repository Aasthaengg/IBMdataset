a = [int(input()) for _ in range(5)]
k = int(input())

for i in range(5):
	for j in range(i,5):
		if a[j] -a[i] > k:
			print(":(")
			exit()
print("Yay!")