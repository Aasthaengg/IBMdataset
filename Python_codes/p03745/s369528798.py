n = int(input())
A = list(map(int, input().split()))
count = 1
direction = 0
for a, b in zip(A, A[1:]):
	dif = b - a
	if direction == 0:
		if dif > 0:
			direction = 1
		elif dif < 0:
			direction = -1
	elif (direction == 1 and dif < 0) or (direction == -1 and dif > 0):
		count += 1
		direction = 0
print(count)