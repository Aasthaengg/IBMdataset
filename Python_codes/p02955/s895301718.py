n, k = map(int, input().split())
arr = list(map(int, input().split()))

# n, k = 8, 7
# arr = list(map(int, "1 7 5 6 8 2 6 5".split()))

add = sum(arr)

def check(factor):
	mod_factor = [x%factor for x in arr]
	mod_factor.sort(reverse = True)
	p = sum(mod_factor)//factor
	# print('p: ', p, 'factor:',factor, 'sum: ', sum(mod_factor))
	# print('mod_factor: ', mod_factor)
	# print(mod_factor[:p])
	c = sum(factor - mod_factor[i] for i in range(p))
	return c <= k

ans = i = 1
while i*i <= add:
	if add % i == 0:
		if check(i):
			ans = max(ans, i)
		if check(add//i):
			ans = max(ans, add//i)
	i += 1
print(ans)