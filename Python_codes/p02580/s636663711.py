h,w,m=map(int,input().split())
row=[0]*h
col=[0]*w
s=[]
for _ in range(m):
	x,y=map(int,input().split())
	row[x-1]+=1
	col[y-1]+=1
	s.append([x-1,y-1])
a,b=max(row),max(col)
aa=row.count(a)
bb=col.count(b)
c=0
for x,y in s:
	if row[x]==a and col[y]==b:c+=1
if c<aa*bb:print(a+b)
else:print(a+b-1)