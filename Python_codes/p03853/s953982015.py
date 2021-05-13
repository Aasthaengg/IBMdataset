h,w=map(int,input().split())
c=[list(input().split()) for _ in range(h)]
a=[]
for i in range(h):
	a.append(c[i])
	a.append(c[i])
for j in a:
	print(*j)