n =int(raw_input())

q = 1
mod = 10 ** 9 + 7
for u in range(2, n+1):
	q *= u
	q %= mod
print q