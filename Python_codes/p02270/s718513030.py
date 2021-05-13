import sys

def check_alloc(weights, cnt, cpct):	
	num = 1
	cur = 0
	for i in range(len(weights)):
		w = weights[i]
		if cur + w > cpct:
			cur = w
			num += 1
			if num > cnt or cur > cpct:
				return False
		else:
			cur += w
	return True

n, k = map(int, input().split())
weights = [0] * n
sum = 0
maxi = 0
for i in range(n):
	weight = int(input())
	weights[i] = weight
	sum += weight
	maxi = max(maxi, weight)

if k == 1:
	print(sum)
	sys.exit()

start = maxi
end = sum
mid = 0
while start <= end:
	mid = int(start + (end - start) / 2)
	can_alloc = check_alloc(weights, k, mid)
	if can_alloc == False:
		start = mid + 1
	else:
		if start == end: break
		end = mid

print(mid)

