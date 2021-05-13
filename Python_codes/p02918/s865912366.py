import heapq
t = 1
def max(a,b):
	if a > b:
		return a
	return b
def min(a,b):
	if a < b:
		return a
	return b

while t > 0:
	t -= 1
	n,k = map(int,input().split())
	# n = int(input())
	# a = list(map(int,input().strip().split()))[0:n]
	# b = list(map(int,input().strip().split()))[0:n]
	# c = list(map(int,input().strip().split()))[0:n-1]
	s = input()
	i = 0
	ans = 0
	c = 0
	d = 0
	while(i < n):
		j = i
		# c += 1
		if s[i] == 'R':
			c += 1
		else:
			d += 1
		while j+1 < n and s[j+1] == s[i]:
			j += 1
		l = j-i+1
		ans += (l-1)
		i = j+1
	c = min(c,d)
	# print()
	if s[0] == s[n-1]:
		if k < c:
			# print("a")
			ans += 2*k
		else:
			# print("b")
			ans += 2*(c)
	else:
		if k < c:
			# print("a")
			ans += 2*k
		else:
			ans += 2*(c-1)
			ans += 1
		# ans += 1
		# ans += 1
	print(ans)
