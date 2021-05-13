import itertools
n,m = map(int,input().split())

s = [[] for _ in range(m)]

for i in range(m):
	k,*t = map(int,input().split())
	for j in t:
		s[i].append(j-1)

targ = list(map(int,input().split()))
ans = 0
#print(s)

for i in itertools.product(range(2), repeat=n):
	tmpl = [0]*m
	
	for j in range(m):
		for k in s[j]:
			tmpl[j] += i[k]
	
	mode = 1
	
	for j in range(m):
		if tmpl[j]%2 != targ[j]:
			mode = 0
			break
	
	if mode:
		ans += 1

print(ans)