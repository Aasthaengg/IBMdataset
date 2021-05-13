t = int(input())
par = [0, 0]
for i in range(t):
	p, t = map(int, input().split())
	if p >= par[0] and t >= par[1]:
		par = [p, t]
	else:
		n = max((par[0]-1)//p + 1, (par[1]-1)//t +1)
		par = [p*n, t*n]
print(sum(par))
