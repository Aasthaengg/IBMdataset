n,l=map(int,input().split())
t=[l+i for i in range(n)]
tot = sum(t)
ans = tot - t[0]
mn = float('inf')
for i in range(n):
	tmp = tot-t[i]
	if abs(tmp-tot)<mn:
		mn = abs(tmp-tot)
		ans = tmp
		
print(ans)
