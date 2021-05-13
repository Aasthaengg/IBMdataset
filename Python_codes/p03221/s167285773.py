n,m=map(int,input().split())

items=[]
for i in range(m):
    p,y=map(int,input().split())
    items.append((p,y,i))
items.sort()

now=0
p1=items[0][0]
ans=[]
for p,y,ind in items:
    if p==p1:
        now+=1
        tmp=str(p*10**6+now)
        tmp=(12-len(tmp))*"0"+tmp
        ans.append((ind,tmp))
    else:
        now=1
        p1=p
        tmp=str(p*10**6+now)
        tmp=(12-len(tmp))*"0"+tmp
        ans.append((ind,tmp))

ans.sort()
for _ , j in ans:
    print(j)