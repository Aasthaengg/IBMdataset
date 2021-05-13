MOD = 1000000007
def power(a, b):
	if b == 0:
		return 1
	elif b == 1:
		return a % MOD
	elif b % 2 == 0:
		return (power(a, b//2) ** 2) % MOD
	else:
		return (power(a, b//2) ** 2 * a) % MOD
 
L = input()
N = len(L)
ans = 0
cou = 0
for i in range(N):
    if L[i] == "1":
        if i == 0:
            ans += (power(3, N-1-i) + 2) * (power(2, cou))
            ans %= MOD
            cou += 1
        else:
            ans += (power(3, N-1-i) + 1) * (power(2, cou))
            ans %= MOD
            cou += 1
print(ans)