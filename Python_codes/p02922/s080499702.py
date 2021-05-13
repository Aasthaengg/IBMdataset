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
	a,b = map(int,input().split())
	i = 1
	c = a
	if b == 1:
		print(0)
		exit(0)
	while a < b:
		if(i == 0):
			a = a+(c)
		else:
			a = a+(c-1)
		i += 1
	print(i)
