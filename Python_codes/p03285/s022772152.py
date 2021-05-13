
def f(n):
	for i in range(0, n/4 + 1):
		for j in range(0, n / 7 + 1):
			if 4*i + 7 * j == n:
				return True

	return False
print 'Yes' if f(int(raw_input())) else 'No'