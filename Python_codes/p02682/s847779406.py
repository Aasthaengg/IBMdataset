a,b,c,k = map(int, raw_input().split())
t = [a,b,c]
s = 0
h = {0:1, 1:0, 2:-1}
for i,e in enumerate(t): 
	s += min(k, e) * h[i]
	k-= min(e,k)
print s