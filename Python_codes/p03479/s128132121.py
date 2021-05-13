x,y=map(int,input().split())
ans=1
while x*2 <= y:
    ans= ans+1
    x=x*2
print(ans)