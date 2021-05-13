n,m=map(int,input().split())
d={}
A=[0]*n
B=[0]*n
for i in range(n):
    A[i],B[i]=map(int,input().split())
    d[str(i)]=A[i]
a=sorted(d.items(),key=lambda x:x[1])
ans=0
for i in range(n):
    if m>B[int(a[i][0])]:
        m-=B[int(a[i][0])]
        ans+=a[i][1]*B[int(a[i][0])]
    else:
        ans+=a[i][1]*m
        break
print(ans)