a,b,x=map(int,input().split())
n=a//x
m=b//x
ans=m-n
if a%x==0:
    ans+=1
print(ans)