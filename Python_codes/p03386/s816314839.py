a,b,k = map(int,input().split())
ans = []
if (a+k) < b:	
	for i in range(a, a+k):
		ans.append(i)
else:
	for i in range(a, b):
		ans.append(i)
if (b-k) > a:
	for l in range(b-k+1,b+1):
		ans.append(l)
else:
	for l in range(a,b+1):
		ans.append(l)
ans = set(ans)
ans = sorted(ans)

for a in ans:
	print(a)