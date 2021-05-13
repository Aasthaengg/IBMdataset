t = 1
# t = input()
# t = int(t)
def max(a,b):
	if a > b:
		return a
	return b
while t > 0:
	t -= 1
	n,k = map(int,input().strip().split())
	v = list(map(int,input().strip().split()))[0:n]
	# m = {}
	ans = 0
	for i in v:
		if i >= k:
			ans += 1
		# temp = x/i
		# if(x%i != 0):
		# 	temp += 1
		# m[i] += 1
	# ans = 0
	print(ans)
	# rem = 0
