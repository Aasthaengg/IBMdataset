a,b,x=map(int,input().split())
A=a//x
B=b//x
ans=B-A
if a%x==0:
    ans+=1
print(ans)