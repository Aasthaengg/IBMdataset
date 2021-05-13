n , g = map(int , input().split())
pt = []
for i in range(0 , n):
	pt.append(list(map(int , input().split())))
# u need to solve all the problems of some bitmask or 
# solve all the problems of the bitmask and if remaining solve the problem which has higher point
# and is not set 
ans = 10**9+89
for i in range(0 , (1<<n)):
	tot , cnt = 0 , 0 
	partial=-1
	for j in range(0 , n):
		if (i & (1<<j)):
			cnt = cnt+pt[j][0]
			tot = tot + (100)*(j+1)*pt[j][0]+pt[j][1]# solve all the problems
		else:
			partial =j# partial solve and take maximum of it because it is optimal
	if tot<g:# if points still remaining
		a = 100*(partial+1)
		rem = (g-tot+a-1)//a
		if rem>=pt[partial][0]:# ignore u can't solve this problem with this set of problems
			continue
		cnt =cnt+rem
	ans = min(ans, cnt)
print(ans)