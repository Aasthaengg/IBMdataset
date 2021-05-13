n,l=map(int,input().split())
t=[]
tmp=0
for i in range(n):
    k=i+l
    t.append(k)
    tmp+=k
if min(t)>0:
    tmp-=min(t)
if max(t)<0:
    tmp-=max(t)
print(tmp)