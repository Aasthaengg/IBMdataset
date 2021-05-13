from collections import defaultdict
import itertools

def pfact(m):
	pf = {}
	for i in range(2,int(m**0.5)+1):
		while m%i == 0:
			pf[i] = pf.get(i,0) + 1
			m //= i
	if m>1 : pf[m]=1
	return pf

n = int(input())

plist = defaultdict(lambda: 0)
for i in range(2, n+1):
	for j, k in pfact(i).items():
		plist[j] += k

def makediv(n):
	lower_divisors , upper_divisors = [], []
	i = 1
	while i*i <= n:
		if n % i == 0:
			lower_divisors.append(i)
			if i != n // i:
				upper_divisors.append(n//i)
		i += 1
	return lower_divisors + upper_divisors[::-1]

shichigo = set(makediv(75))
shichigo.remove(1)

thelist = [j+1 for j in plist.values()]
thelist.sort()

ansdict = {
	3: 0,
	5: 0,
	15: 0,
	25: 0,
	75: 0
}

for cnt, i in enumerate(thelist):
	for j in range(i+1):
		if j in shichigo:
			ansdict[j] += 1

"""
75
= 5*15
= 3*25
= 3*5*5
"""

ans = 0
ans += ansdict[75]
ans += ansdict[15]*(ansdict[5]-1)
ans += ansdict[25]*(ansdict[3]-1)
ans += ansdict[5]*(ansdict[5]-1)*(ansdict[3]-2)//2
print(ans)