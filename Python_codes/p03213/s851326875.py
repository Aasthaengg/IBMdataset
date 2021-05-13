n = int(input())
def factorize(n,factors):
	d = 2
	orig_n = n
	while d*d <= orig_n and n > 1:
		while n%d==0:
			factors[d] = factors.get(d,0)+1
			n //= d 
		d += 1
	if n > 1:
		factors[n] = factors.get(n,0)+1
def geq(val,factors):
	return len([x for x in factors if factors[x] >= val])

factors = {}
for i in range(1,n+1):
	factorize(i,factors)

ans = 0
ans += geq(74,factors)
ans += geq(24,factors)*(geq(2,factors)-1)
ans += geq(14,factors)*(geq(4,factors)-1)
ans += (geq(4,factors)*(geq(4,factors)-1)//2)*(geq(2,factors)-2)

print(ans)