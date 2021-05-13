def get_ints():
	return map(int, input().split())
def get_list():
	return list(map(int, input().split()))

n = int(input())
dp = [0 for ans in range(10050)]
for x in range(1, 105):
	for y in range(1, 105):
		for z in range(1, 105):
			v = x*x + y*y + z*z + x*y + y*z + z*x
			if v < 10050:
				dp[v] += 1
for i in range(n):
	print(dp[i + 1])