n,k = map(int,raw_input().split())
weights = []
for i in range(n):
	weights.append(int(input()))

def check(p):
	i = 0
	for j in range(k):
		w = 0
		while w + weights[i] < p:
			w += weights[i]
			i += 1
			if i == n:
				return True

	return False

left = 0
right = 100000 * 10000
mid = 0

while right - left > 1 :
	mid = (left + right)/2
	if check(mid):
		right = mid
	else : 
		left = mid

print right-1


