a,b = map(int,input().split())
l = list(map(int,input().split()))
m = sorted(l,reverse=False)
z=0
for i in range(b):
	z=z+m[i]
print(z)