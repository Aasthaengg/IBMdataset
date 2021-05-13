def isprime(num):
	for k in range(2, int(num**0.5)+1):
		if num % k == 0:
			return False
	return True

n = int(input())
pl = []

for i in range(2, 55555):
	if i % 5 == 1:
		if isprime(i):
			pl.append(i)

print(" ".join(list(map(str, pl[0:n]))))