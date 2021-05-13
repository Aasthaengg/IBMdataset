def resolve():
	from collections import deque
	K = int(input())
	q = deque(str(i) for i in range(1, 10))
	cnt = 9
	if K < 10:
		print(K); return
	while True:
		tmp = q.popleft()
		las = int(tmp[-1])
		for i in range(las-1, las+2):
			if 0<=i<=9:
				q.append(tmp + str(i))
				cnt += 1
				if cnt==K:
					print(q.pop()); return
resolve()