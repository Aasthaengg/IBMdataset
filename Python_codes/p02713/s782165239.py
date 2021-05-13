import math
K = int(input())
ans = 0
for i in range(1,K+1):
	for j in range(1,K+1):
		tmp = math.gcd(i,j)
		for n in range(1,K+1):
			ans += math.gcd(tmp,n)
print(ans)