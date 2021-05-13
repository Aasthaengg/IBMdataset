from operator import itemgetter
n,m=map(int,input().split())
a=[""]*m
b=[""]*m
for i in range(m):
    x,l=map(int,input().split())
    a[i]=x*10+5
    b[i]=l*10-5
st=sorted([(a[i],b[i]) for i in range(m)], key=itemgetter(1))
ans=0
last=0
last=-float("inf")
for i in range(m):
    if last<st[i][0]:
        ans+=1
        last=st[i][1]
print(ans)