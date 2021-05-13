n=int(input())
lists=[0]*n
for i in range(n):
    s=int(input())
    lists[i]=(s,i)
a=sorted(lists,key=lambda x:x[0])
uselist=[0]*(n+1)
for i in range(n):
    uselist[i]=a[i][1]

cnt=0
count=1
for i in range(n):
    if uselist[i]<uselist[i+1]:
        count+=1
    else:
        cnt=max(count,cnt)
        count=1
print(n-cnt)