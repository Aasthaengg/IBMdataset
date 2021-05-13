N = int(input())
A = [int(i) for i in input().split()]
a = [0] * ((N + 1) // 2)
for i in A:
	if N % 2:
		if i % 2:
			print(0)
			exit()
	else:
		if i % 2 == 0:
			print(0)
			exit()
	a[i // 2] += 1
if N % 2:
	if any(i != 2 for i in a[1:]) or a[0] != 1:
		print(0)
		exit()
else:
	if any(i != 2 for i in a):
		print(0)
		exit()
print(2 ** (N // 2) % 1000000007)