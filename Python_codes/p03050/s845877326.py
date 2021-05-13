n = int(input())

def makediv(n):
	lower_divisors , upper_divisors = [], []
	i = 1
	while i*i <= n:
		if n % i == 0:
			lower_divisors.append(i)
			if i != n // i:
				upper_divisors.append(n//i)
		i += 1
	return lower_divisors + upper_divisors[::-1]

ans = 0
for i in makediv(n):
	targ = i-1
	if targ != 0:
		if n // targ == n % targ:
			ans += targ
print(ans)