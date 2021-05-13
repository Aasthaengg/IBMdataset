n,k=map(int,input().split())

a=list(map(int,input().split()))

l=[1]
di={}
di[1]=1

for i in a:
    b=a[l[-1]-1]
    if b in di:
        x=b
        break
    l.append(b)
    di[b]=1
t1=0
for j in l:
    if j==x:
        break
    else:
        t1+=1

t2=len(l)-t1
if k<=t1:
    print(l[k])

else:
    aa=(k-t1)%t2
    print(l[t1+aa])