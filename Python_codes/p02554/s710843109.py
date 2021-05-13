n = int(input())
ans = 1
ans1 = 1
ans2 = 1
mod = 1000000007
for i in range(n):
	ans = (ans*10)%mod
	ans2 = (ans2*8)%mod
	ans1 = (ans1*9)%mod
ans = (ans - ans1 + mod)%mod
ans = (ans - ans1 + mod)%mod
ans = (ans + ans2)%mod
print(ans)
