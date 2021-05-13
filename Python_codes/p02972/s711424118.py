n = int(input())
a = list(map(int,input().split()))
b = []
c = [0 for _ in range(n)]

def make_divisors(n):
	lower_divisors , upper_divisors = [], []
	i = 1
	while i*i <= n:
		if n % i == 0:
			lower_divisors.append(i)
			if i != n // i:
				upper_divisors.append(n//i)
		i += 1
	return lower_divisors + upper_divisors[::-1]

#半分より上は, すべてa通り.
for i in range(1,n+1)[::-1]:
	if c[i-1] % 2 != a[i-1]:
		b.append(i)
		for j in make_divisors(i):
			c[j-1] += 1
print(len(b))
print(" ".join(list(map(str, b))))