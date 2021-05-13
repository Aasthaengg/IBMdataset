import itertools

h,w,k=map(int,input().split())
matrix=[]
for i in range(h):
	s=list(input())
	matrix.append(s)
hlist=[]
for i in range(h):
	hlist.append(i)
wlist=[]
for i in range(w):
	wlist.append(i)
rows=[]
cols=[]
for i in range(h+1):
	obj=itertools.combinations(hlist, i)
	rows+=list(obj)
for i in range(w+1):
	obj=itertools.combinations(wlist, i)
	cols+=list(obj)
ans=0
for i in rows:
	for j in cols:
		count=0
		for a in range(h):
			for b in range(w):
				if(matrix[a][b]=='#' and a not in i and b not in j):
					count+=1
		if(count==k):
			ans+=1
print(ans)