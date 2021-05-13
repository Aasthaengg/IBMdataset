import collections
n,s = int(raw_input()), raw_input()

def f(k, s):	
 	cc,q = collections.Counter(), collections.deque()
	for j in range(k - 1, len(s)):
		q.append(s[j - k + 1:j+1])
		if len(q) == k + 1: cc[q.popleft()] += 1
		if q[-1] in cc: return True	
	return False

lo,hi = 0, n/2
while(lo < hi):
	med = (lo + hi + 1) / 2
	if f(med, s):  lo = med
	else:hi = med - 1
print lo