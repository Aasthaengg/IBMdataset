n,m = map(int, raw_input().split())
s = [map(int, raw_input().split()) for _ in range(m)]
c = 0
s.sort()
cur = s[0]
for u,v in s[1:]:
	if cur == []:
		cur = [u,v]
	if cur[1] <= u:
		cur = [u,v]
		c += 1 
	else:
		cur[0] = max(u, cur[0])
	 	cur[1] = min(v, cur[1])
		if cur[1] - cur[0] == 0: 
			c +=1
			cur = []
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