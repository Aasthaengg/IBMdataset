A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[list(map(int,input().split())) for i in range(M)]
d = 0
e = 0
aa=sorted(a)
bb=sorted(b)

e=aa[0]+bb[0]

for i in range(M):
	d=a[c[i][0]-1]+b[c[i][1]-1]-c[i][2]
	if d<e:
		e=d

print(e)