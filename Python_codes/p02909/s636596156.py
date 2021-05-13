import math
t = 1
# t = input()
# t = int(t)
def max(a,b):
	if a > b:
		return a
	return b
while t > 0:
	t -= 1
	s = input()
	ans = ""
	if s == "Sunny":
		ans = "Cloudy"
	elif s == "Cloudy":
		ans = "Rainy"
	else:
		ans = "Sunny"
	print(ans)
	# n = int(input())
	# v = list(map(int,input().strip().split()))[0:n]
	# # m = {}
	# l = []
	# for i in range(n):
	# 	l.append(0)
	# # ans = 0
	# j = 1
	# for i in v:
	# 	l[i-1] = j
	# 	j += 1
	# # print(ans)
	# for i in l:
	# 	print(i,end=" ")
