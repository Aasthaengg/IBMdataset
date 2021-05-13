a, b = map(int, input().split())
nums = [a, b, a+b]
r = 'Impossible'
for num in nums:
	if num % 3 == 0:
		r = 'Possible'
		break
print(r)