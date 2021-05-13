n,m = map(int, raw_input().split())
s = [map(int, raw_input().split()) for _ in range(m)]
c = 0
s.sort()
cur = []
for u,v in s:
	if cur == []:
		cur = [u,v]
	if cur[1] <= u:
		cur = [u,v]
		c += 1 
	else:
		cur = [max(u, cur[0]),min(v, cur[1])]
print c + (1 if cur else 0)
"""
---- ------
     4    9
       ---
       5 6
       ------?
       5 

       5 ----- 10
"""