n = int(input())
A = list(map(int, input().split()))
count = 0
for a in A:
	while a % 2 == 0:
		count += 1
		a //= 2
print(count)