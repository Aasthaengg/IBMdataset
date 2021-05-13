import math
N = int(input())
ans = []
ctr = 0

# "5で割って余りが1になる数" を5個足せば、5で割れる（5の倍数になる）
# 5の倍数のうち、5だけは素数である
# 素数は2以上であるから、5個足すと必ず5より大きい数になる

def is_prime(n):
	if n == 2: return True
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0: return False
	return True

for i in range(6, 55555 + 1, 5): # mod5で余りが1になる数を探す
	if is_prime(i):
		ans.append(i)
		ctr += 1
	if ctr == N: break
	
print(*ans)