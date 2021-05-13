n = int(input())
v = list(map(int,input().split()))

for i in range(n-1):
	x = min(v)
	v.remove(x)
	y = min(v)
	v.remove(y)
	v.append((x+y)/2) 

print(v[0])