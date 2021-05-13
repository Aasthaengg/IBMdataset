from math import sqrt
n=int(input())
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
l=make_divisors(n)
if len(l)%2==0:
	print((l[len(l)//2]+l[(len(l)//2)-1])-2)
elif len(l)%2==1:
	print(int((sqrt(n)*2)-2))