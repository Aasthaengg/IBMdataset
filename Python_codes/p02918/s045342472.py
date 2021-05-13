n,k = map(int,input().split())
s = list(input())
c = 0
a = 0

for i in range(n-1):
	if s[i] == s[i+1]:
		c += 1
	if a < k:
		if s[i] == 'R' and s[i+1] == 'L':
			c += 2
			a += 1
if a < k and a + 2 <= k:
	if s[0] == 'L':
		c += 1
	if s[-1] == 'R':
		c += 1
if a < k and a + 1 >= k:
	if s[0] == 'L' or s[-1] == 'R':
		c += 1
print(min(c,n-1))