def solve_israil(n):
	if 400<=n and n<=599:
		return 8
	elif 600<=n and n<=799:
		return 7
	elif 800<=n and n<=999:
		return 6
	elif 1000<=n and n<=1199:
		return 5
	elif 1200<=n and n<=1399:
		return 4
	elif 1400<=n and n<=1599:
		return 3
	elif 1600<=n and n<=1799:
		return 2
	else:
		return 1
									


n=int(input())
print(solve_israil(n))