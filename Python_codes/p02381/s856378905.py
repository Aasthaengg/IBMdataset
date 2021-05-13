import math

while True:
	n = eval(input())
	if n == 0:
		break
	s = [eval(x) for x in input().split()]
	m = sum(s)/n
	sd = math.sqrt(sum([(x-m)**2 for x in s])/n)
	print(sd)