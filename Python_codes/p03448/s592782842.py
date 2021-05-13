a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
x = int(raw_input())

def dfs(x, i, a, b , c):
  	if x < 0:
  		return 0
  	if x == 0:
  		return 1
  	
  	if i == 3:
  		return 1 if x == 0 else 0
  	r = 0
  	m = {0:a,1:b,2:c}
  	v = {0:500,1:100,2:50}

  	for k in range(0, m[i] + 1):
  		r += dfs(x - k * v[i], i+1, a,b,c)
  	return r

print dfs(x,0,a,b,c)
