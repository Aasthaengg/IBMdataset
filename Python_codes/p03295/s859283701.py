n,m = map(int, raw_input().split())
s,c = [map(int, raw_input().split()) for _ in range(m)], 1
s.sort()
cur = s[0]
for u,v in s[1:]:
	if cur[1] <= u:
		cur,c = [u,v], c + 1 
	else: cur = [max(u, cur[0]),min(v, cur[1])]
print c