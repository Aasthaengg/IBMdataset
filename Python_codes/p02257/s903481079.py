n = int(raw_input())

def isprime(m):
	if m == 2:
		return 1
	elif m < 2 or m % 2 == 0:
		return 0
	else:
		p = 3
		while p <= m**0.5:
			if m % p == 0:
				return 0
			p = p + 2
		return 1

cnt = 0
for i in range(n):
	cnt += isprime(int(raw_input()))
	#print("*{:}".format(cnt))

#print("")
print cnt