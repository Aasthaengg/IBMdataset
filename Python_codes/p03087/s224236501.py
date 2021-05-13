n,q = map(int,input().split())
s = input()
l = [0]*q
r = [0]*q
for i in range(q):
	l[i],r[i] = map(int,input().split())
c = [0]*(len(s)+1)
for i in range(len(s)-1):
	if s[i] == 'A' and s[i+1] == 'C':
		c[i+1] += c[i] + 1
	else:
		c[i+1] = c[i]
for i in range(q):
	print(c[r[i]-1]-c[l[i]-1])