n,m,x=map(int,input().split())
a=[int(i)for i in input().split()]
res=0
tmp=[0,0]
for i in a:
    if i<x:
        tmp[0]+=1
    else:
        tmp[1]+=1
res=min(tmp)
print(res)