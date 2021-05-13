cache = {}
def fib(x):
	if x in cache:
		return cache[x]
	elif x == 0 or x == 1:
		return 1
	else:
		v = fib(x - 1) + fib(x - 2)
		cache[x] = v
		return v

x = input()
print fib(x)