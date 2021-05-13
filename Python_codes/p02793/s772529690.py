N = input()
A = [int(x) for x in input().split()]

def gcd(a, b):
	return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
	return a // gcd(a, b) * b

L = 1

for a in A:
	L = lcm(L, a)

print(sum(L // a for a in A) % (10 ** 9 + 7))
