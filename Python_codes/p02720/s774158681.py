from collections import deque

K = int(input())
q = deque()

for i in range(1, 10):
	q.append(i)

k = 0
while True:
	n = q.popleft()
	k += 1
	if k == K:
		break
	if (n % 10) % 10 != 0:
		q.append(10 * n + (n % 10) - 1)
	q.append(n * 10 + (n % 10))
	if (n % 10) % 10 != 9:
		q.append(10 * n + (n % 10) + 1)
print(n)