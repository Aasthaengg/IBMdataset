m,v = {i: int(raw_input()) for i in range(3)}, {0:500,1:100,2:50}
x = int(raw_input())

def dfs(x, i, m, v):
  	if x < 0: return 0
  	if x == 0 or i == 3: 
  		return 1 if x == 0 else 0   	
  	r = 0
  	for k in range(0, m[i] + 1): r += dfs(x - k * v[i], i + 1, m, v)
  	return r
print dfs(x,0,m,v)
