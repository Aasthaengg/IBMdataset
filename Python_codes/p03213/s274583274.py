import math

N = int(input())

prime = [0 for _ in range(47 + 1)]
lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

for i in range(2, N + 1):
	num = i
	# 素因数分解
	for p in lst:
		while True:
			if num % p == 0:
				num //= p
				prime[p] += 1
			else: break
			if num == 1: break
		

_75 = 0
_25 = 0
_15 = 0
_5 = 0
_3 = 0

for i in range(len(prime)):
	if prime[i] >= 2:
		_3 += 1
	if prime[i] >= 4:
		_5 += 1
	if prime[i] >= 14:
		_15 += 1
	if prime[i] >= 24:
		_25 += 1
	if prime[i] >= 74:
		_75 += 1
		
def comb(a, b):
	return math.factorial(a) / (math.factorial(b) * math.factorial(a - b))
		
ans = 0
ans += _75
ans += (_3 - 1) * _25 # かけられている数で1引いているのは、かける数で使っているものをかけられる数でも使う場合を除くため
ans += (_5 - 1) * _15
if _5 >= 2:
	ans += (_3 - 2) * comb(_5, 2)

print(int(ans))