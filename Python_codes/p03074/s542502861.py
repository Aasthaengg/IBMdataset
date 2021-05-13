import collections
n,k = map(int, raw_input().split(' '))
s = map(int,list(raw_input()))
stack = []
count,i,j = 0,0,0


while(j < len(s)):
	while(j < len(s) and s[j] == s[i]): j += 1
	stack.append((s[i], j - i))
	i = j
r = 0
cl = 0
q = collections.deque([])
for t,l in stack:
	q.append((t,l))
	cl += l
	if t == 0: k -= 1
	while(k < 0 and q):
		tu,tl = q.popleft()
		cl -= tl
		if tu == 0: k +=1

	r = max(cl, r)
print r