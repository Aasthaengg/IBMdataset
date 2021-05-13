from fractions import gcd
a,b = map(int,input().split())

def pfact(m):
	pf = {}
	for i in range(2,int(m**0.5)+1):
		while m%i == 0:
			pf[i] = pf.get(i,0) + 1
			m //= i
	if m>1 : pf[m]=1
	return pf


"""
最大公約数を素因数分解すればいけそう？
"""

target = gcd(a,b)
pftarg = pfact(target).items()
print(len(pftarg)+1)