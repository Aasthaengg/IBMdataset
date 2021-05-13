N=int(input())
a=list(map(int,input().split()))
M=max(a)
m=min(a)
iM=a.index(M)+1
im=a.index(m)+1
ans=[]
if m>=0:
    flag="+"
elif M<=0:
    flag="-"
elif abs(M)>=abs(m):
    flag="++"
else:
    flag="--"
if flag=="++":
    for i in range(N):
        if a[i]<0:
            a[i]=a[i]+M
            ans.append([iM,i+1])
    flag="+"
if flag=="--":
    for i in range(N):
        if a[i]>0:
            a[i]=a[i]+m
            ans.append([im,i+1])
    flag="-"   
if flag=="+":
    for i in range(N-1):
        M=max(a[:i+1])
        iM=a.index(M)+1
        if a[i]>a[i+1]:
            a[i+1]=a[i+1]+M
            ans.append([iM,i+2])
if flag=="-":
    for i in range(N-2,-1,-1):
        m=min(a[i+1:])
        im=a.index(m)+1
        if a[i]>a[i+1]:
            a[i]=a[i]+m
            ans.append([im,i+1])
print(len(ans))
for i in ans:
    print(i[0],i[1])