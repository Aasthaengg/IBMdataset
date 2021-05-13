h,w,m=map(int,input().split())
row=[0 for i in range(h)]
col=[0 for i in range(w)]
a=[]
for i in range(m):
    r,c=map(lambda x:int(x)-1,input().split())
    a.append([r,c])
    row[r]+=1
    col[c]+=1
rmax=max(row)
cmax=max(col)
ans=rmax+cmax
flag=row.count(rmax)*col.count(cmax)
for i,j in a:
    if(row[i]==rmax and col[j]==cmax):
        flag-=1
if(flag==0):
    ans-=1
print(ans)