import heapq
t = 1
def max(a,b):
	if a > b:
		return a
	return b
while t > 0:
	t -= 1
	n,k,q = map(int,input().split())	
	v = []
	l = []
	# v = list(map(int,input().strip().split()))[0:n]
	for i in range(q):
		p = int(input().strip())
		v.append(p)
	for i in range(n):
		l.append(0)
	for i in v:
		l[i-1] += 1
	# print(l)
	for i in range(n):
		if(l[i] <= q-k):
			print("No")
		else:
			print("Yes")
	# for i in range(n):
	# 	v[i] = -v[i]
	# heapq.heapify(v)
	# for i in range(m):
	# 	x = heapq.heappop(v)
	# 	x = -x
	# 	x = x//2
	# 	heapq.heappush(v,-x)
	# ans = 0
	# for i in range(n):
	# 	ans += (-heapq.heappop(v))
	# print(ans)
