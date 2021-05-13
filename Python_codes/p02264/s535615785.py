import collections as cols

n, q = [int(x) for x in input().split()]
qu = cols.deque()

for i in range(n):
	tmp = [x for x in input().split()]
	qu.append([tmp[0], int(tmp[1])])

num = n
t = 0

while num > 0:
	tmp = qu.popleft()
	if tmp[1] > q:
		t += q
		qu.append([tmp[0], tmp[1] - q])
	else:
		t += tmp[1]
		num -= 1
		print(tmp[0], t)