n, a, k = map(int, input().split())

if a >= k:
	max = k
else:
	max = a

min = a + k - n

if min < 0:
	min = 0

print(max, min)