import collections
n = int(raw_input())
s = raw_input()

def f(k, s):	
	if k == 0:
		return True
 	cc = collections.Counter()
	q = collections.deque()
	for j in range(k - 1, len(s)):
		q.append(s[j - k + 1:j+1])
		if len(q) == k + 1:
			u = q.popleft()
			cc[u] += 1
		if s[j- k+1:j+1] in cc:
			return True	
	return False
lo,hi = 0, n/2 + 1
while(lo < hi):
	med = (lo + hi + 1) / 2
	if f(med, s):
		lo = med
	else:
		hi = med - 1

print lo