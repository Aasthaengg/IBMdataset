n=int(input())
b=list(map(int,input().split()))
a1,a2=[0]*n,[0]*n
a1[0]=b[0]
a1[-1]=b[-1]
for i in range(1,n-1):
    if b[i-1]<b[i]:
        a1[i]=b[i-1]
    else:
        a1[i]=b[i]
a2[0]=b[0]
a2[-1]=b[-1]
for i in range(n-2,0,-1):
    if b[i-1]>b[i]:
        a2[i]=b[i]
    else:
        a2[i]=b[i-1]
ans=0
for i,j in zip(a1,a2):
    ans+=min(i,j)
print(ans)