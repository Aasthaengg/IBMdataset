n = int(raw_input())
ais,res = [0] + map(int, raw_input().split()) ,[0 for _ in range(n +1)]
for u in range(n, 0, -1):
	c,cumul = u,0
	while(c <= n):
		cumul += res[c]
		c += u
	if ais[u] != (cumul % 2):  res[u] = 1
s = sum(res)
print s
if s: print ' '.join([str(i) for i in range(len(res)) if res[i] == 1])