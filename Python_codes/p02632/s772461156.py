k = int(input())
s = input()
mod = 10**9+7
maxn = 2000005
fact = [0 for i in range(maxn)]
fact[0] = 1
for i in range(1,maxn):
	fact[i] = (i*fact[i-1])%mod
n = len(s)
ans = pow(26,n+k,mod)
for m in range(n):
	calc = (fact[n+k]%mod * pow(fact[m],mod-2,mod))%mod
	calc = (calc * pow(fact[n+k-m],mod-2,mod))%mod
	p = pow(25,n+k-m,mod)
	val = (calc*p)%mod
	ans = (ans-val)%mod
print(ans%mod)