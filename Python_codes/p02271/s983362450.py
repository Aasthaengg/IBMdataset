
def solve(a, m):
	dict = {}
	return solve_(a, 0, m, dict)

def solve_(a, i, m, dict):
	res = False
	key = str(i) + '-' + str(m)
	if key in dict:
		res = dict[key]
	elif m == 0:
		res = True
	elif i >= len(a):
		res = False
	else:
		res1 = solve_(a, i + 1, m, dict)
		res2 = solve_(a, i + 1, m - a[i], dict)
		res = res1 or res2
	dict[key] = res
	return res

n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
for i in range(q):
	if solve(a, m[i]):
		print('yes')
	else:
		print('no')

