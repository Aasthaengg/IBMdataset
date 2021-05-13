n = input()
lis = map(int, raw_input().split())
min = 1000000
max = - min
sum = 0
for t in lis:
	sum += t
	if min > t:
		min = t
	if max < t:
		max = t

print min, max, sum