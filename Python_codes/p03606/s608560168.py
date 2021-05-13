n=int(input())
ans=0
while n>0:
    a,b=map(int,input().split())
    ans+=b-a+1
    n-=1
print(ans)