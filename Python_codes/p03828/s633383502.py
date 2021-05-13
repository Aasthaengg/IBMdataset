def compute(n):
	prime = [ True for i in range(0, n+1)]
	res = []
	for i in range(2, n+1):
		if prime[i]==True:
			res.append(i)
			for j in range(i , n+1,i):
				prime[j]=False
	return res

mod = 10**9+7
n = int(input())
res = compute(n)
tot = 1
for i in res:
	now = 0
	p =n
	while p>0:
		now = now+(p//i)
		now = now%mod
		p=p//i
	tot = (tot % mod)*((now+1)%mod)
	tot = tot%mod
print(tot)