import itertools
import fractions
n=int(input())
a=list(map(int,input().split()))
a.sort()
mina=a[0]
ans = 10**18
for i in range(n):
	ans = min(ans, fractions.gcd(a[i], mina))
print(ans)