def solve(arr, target):
	memo = {}
	return solve_rec(0, arr, target, memo)

def solve_rec(i, arr, target, memo):

	res = False

	key = str(i) + '-' + str(target)
	if key in memo:
		res = memo[key]
	elif target == 0:
		res = True
	elif i >= len(arr):
		res = False
	else:
		res1 = solve_rec(i + 1, arr, target, memo)
		res2 = solve_rec(i + 1, arr, target - arr[i], memo)
		res = res1 or res2

	memo[key] = res		
	return res

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
targets = list(map(int, input().split()))
for i in range(q):
	res = solve(arr, targets[i])
	if res == True:
		print('yes')
	else:
		print('no')
