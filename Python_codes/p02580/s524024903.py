
n,m,t=map(int,input().split())

grid=[]

row=[0]*n
col=[0]*m

for _ in range(t):
    x,y=map(int,input().split())
    grid.append((x-1,y-1))
    row[x-1]+=1
    col[y-1]+=1

prow=[]
pcol=[]
qr=max(row)
for i in range(n):
    if row[i]==qr :
        prow.append(i)

qc=max(col)
for i in range(m):
    if col[i]==qc :
        pcol.append(i)

num=len(prow)*len(pcol)
ans=qr+qc
for i in grid:
    if row[i[0]]==qr and col[i[1]]==qc :
        num-=1
if num>0:
    print(ans)
else:
    print(ans-1)