n = int(input())
c = input().split()

cb = c[:]
for i in range(n):
	for j in range(n-1,i,-1):
		if cb[j][1] < cb[j-1][1]:
			cb[j-1],cb[j] = cb[j],cb[j-1]
print(*cb)
print('Stable')

cs = c[:]
for i in range(n):
	m = min(range(i,n), key=lambda j: cs[j][1])
	if i != m:
		cs[i],cs[m] = cs[m],cs[i]
print(*cs)
print('Stable' if cb == cs else 'Not stable')
