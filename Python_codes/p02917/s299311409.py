import heapq
t = 1
def max(a,b):
	if a > b:
		return a
	return b
while t > 0:
	t -= 1
	# n = map(int,input().split())
	n = int(input())
	# a = list(map(int,input().strip().split()))[0:n]
	# b = list(map(int,input().strip().split()))[0:n]
	c = list(map(int,input().strip().split()))[0:n-1]
	b = []
	for i in range(n):
		b.append(0)
	b[0] = c[0]
	b[n-1] = c[n-2]
	for i in range(1,n-1):
		b[i] = min(c[i],c[i-1])
	ans = 0
	for i in range(n):
		ans += b[i]
	print(ans)
	# print(n*n*n)
	# m = 1000
	# i = 0
	# while i < n:
	# 	j = i
	# 	while j+1 < n and v[j+1] >= v[j]:
	# 		j += 1
	# 	x = m//v[i]
	# 	m = m%v[i]
	# 	temp = x*v[j]
	# 	m += temp
	# 	i = j+1
	# print(m)
