import heapq

K, T = map(int, input().split())
a = [int(i) for i in input().split()]
b = [[0 for j in range(2)] for i in range(T)]
for i in range(T):
	b[i][0] = a[i] * -1
	b[i][1] = i
heapq.heapify(b)
ans, c = 0, -1
while len(b):
	d = heapq.heappop(b)
	if c == d[1]:
		if not len(b):
			ans += 1
			c = d[1]
			d[0] += 1
			if d[0]:
				heapq.heappush(b, d)
		else:
			e = heapq.heappop(b)
			c = e[1]
			e[0] += 1
			heapq.heappush(b, d)
			if e[0]:
				heapq.heappush(b, e)
	else:
		c = d[1]
		d[0] += 1
		if d[0]:
			heapq.heappush(b, d)
print(ans)