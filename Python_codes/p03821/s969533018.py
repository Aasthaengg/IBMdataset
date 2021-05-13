n=int(input())
a,b=[],[]
for _ in range(n):
    A,B=map(int,input().split())
    a.append(A)
    b.append(B)
ans=0
for i in range(n-1,0,-1):
    if a[i]%b[i]!=0: temp=b[i]+b[i]*(a[i]//b[i])-a[i]
    else: temp=0
    ans+=temp
    a[i-1]+=ans
if a[0]%b[0]!=0: ans+=b[0]+b[0]*(a[0]//b[0])-a[0]
print(ans)