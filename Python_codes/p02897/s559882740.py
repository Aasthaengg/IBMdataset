t = 1
# t = input()
# t = int(t)
def max(a,b):
	if a > b:
		return a
	return b
while t > 0:
	t -= 1
	n = input()
	n =int(n)
	ans = 0.5
	if n%2 == 1:
		# print("a")
		ans = (n//2 + 1.0)/(n*1.0)
	print(ans)
	# n,x = map(int,input().strip().split())
	# v = list(map(int,input().strip().split()))[0:n]
	# m = {}
	# for i in v:
	# 	temp = x/i
	# 	if(x%i != 0):
	# 		temp += 1
	# 	m[i] += 1
	# ans = 0
	# rem = 0
