kosuu = int(input())
dp = list(map(int,input().split()))
ans = []
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return set((lower_divisors + upper_divisors[::-1])[:-1])
for i in range(kosuu):
	hako = kosuu - i
	if dp[hako-1] == 1:
		for j in make_divisors(hako):
			dp[j-1] ^= 1
		ans.append(str(hako))
print(len(ans))
print(' '.join(ans))