n = int(input())

def isprime(n):
	if n == 1:
		return False
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False
	return True

ansl = []

for i in range(1, n+1):
	if isprime(i):
		tmp = 1
		tmpans = 0
		while True:
			youso = n // (i**tmp)
			tmpans += youso
			if youso == 0:
				break
			tmp += 1
		ansl.append(tmpans)

ans = 1
mod = 10**9+7

for i in ansl:
	ans = ans * (i+1) % mod

print(ans)