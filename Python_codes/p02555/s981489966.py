MOD = 10**9 + 7
list_size = 200001

f_list = [1] * list_size
f_r_list = [1] * list_size

for i in range(list_size-1):
	f_list[i+1] = (f_list[i] * (i+1)) % MOD

f_r_list[-1] = pow(f_list[-1], MOD - 2, MOD)

for i in range(list_size-2, -1, -1):
	f_r_list[i] = (f_r_list[i+1] * (i+1)) % MOD

def comb(n, r):
	if n < r or r < 0:
		return 0
	elif n == 0 or r == 0 or n == r:
		return 1
	else:
		return (f_list[n] * f_r_list[n-r] * f_r_list[r]) % MOD 

s = int(input())
ans = 0
for i in range(1, s//3+1):
	t = s - 3*i
	ans += comb(t+i-1, i-1)
	ans %= MOD
print(ans)