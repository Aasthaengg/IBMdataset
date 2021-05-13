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
	# a,b = map(int,input().split())
	n = int(input())
	v = list(map(int,input().strip().split()))[0:n]
	i = 0
	ans = 0
	while i < n:
		j = i
		while j+1 < n and v[j+1] <= v[j]:
			j += 1
		l = j-i+1
		ans = max(ans,l)
		i = j+1
	print(ans-1) 