import collections
n = int(raw_input())
mod = ( 10 ** 9 ) + 7
def f(u):
	cu = collections.Counter()
	cur = 2
	while(u != 1):
		if u % cur == 0:
			while(u % cur == 0):
				cc[cur] +=1
				u/= cur
		cur +=1
	return cu
cc = collections.Counter()
for u in range(2, n + 1):
	for k,v in f(u).iteritems(): cc[k]+=cu[k]
ans = 1
for k in cc:
	ans *= (cc[k] + 1) 
	ans %= mod
print ans